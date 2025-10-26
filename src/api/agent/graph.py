from pydantic import BaseModel
from typing import List, Dict, Any, Annotated
from operator import add
from api.agent.agents import agent_node, intent_router_node, ToolCall, RAGUsedContext
from api.agent.utils.utils import get_tool_descriptions
from api.agent.tools import get_formatted_context
from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
import numpy as np


class State(BaseModel):
    messages: Annotated[List[Any], add] = []
    question_relevant: bool = False
    iteration: int = 0
    answer: str = ""
    available_tools: List[Dict[str, Any]] = []
    tool_calls: List[ToolCall] = []
    final_answer: bool = False
    references: Annotated[List[RAGUsedContext], add] = []


#### Routers

def tool_router(state: State) -> str:
    """Decide whether to continue or end"""
    
    if state.final_answer:
        return "end"
    elif state.iteration > 2:
        return "end"
    elif len(state.tool_calls) > 0:
        return "tools"
    else:
        return "end"


def intent_router_conditional_edges(state: State):

    if state.question_relevant:
        return "agent_node"
    else:
        return "end"


#### Workflow

workflow = StateGraph(State)

tools = [get_formatted_context]
tool_node = ToolNode(tools)
tool_descriptions = get_tool_descriptions(tools)

workflow.add_node("agent_node", agent_node)
workflow.add_node("tool_node", tool_node)
workflow.add_node("intent_router_node", intent_router_node)

workflow.add_edge(START, "intent_router_node")

workflow.add_conditional_edges(
    "intent_router_node",
    intent_router_conditional_edges,
    {
        "agent_node": "agent_node",
        "end": END
    }
)

workflow.add_conditional_edges(
    "agent_node",
    tool_router,
    {
        "tools": "tool_node",
        "end": END
    }
)

workflow.add_edge("tool_node", "agent_node")

graph = workflow.compile()


#### Agent Execution function

def run_agent(question: str):

    initial_state = {
        "messages": [{"role": "user", "content": question}],
        "iteration": 0,
        "available_tools": tool_descriptions
    }

    result = graph.invoke(initial_state)

    return result


def run_agent_wrapper(question: str):

    qdrant_client = QdrantClient(url="http://qdrant:6333")

    result = run_agent(question)

    used_context = []
    dummy_vector = np.zeros(1536).tolist()

    for item in result.get("references", []):
        payload = qdrant_client.query_points(
            collection_name="Amazon-items-collection-01-hybrid-search",
            query=dummy_vector,
            using="text-embedding-3-small",
            limit=1,
            with_payload=True,
            query_filter=Filter(
                must=[
                    FieldCondition(
                        key="parent_asin", 
                        match=MatchValue(value=item.id))
                ]
            )
        ).points[0].payload
        image_url = payload.get("image")
        price = payload.get("price")
        if image_url:
            used_context.append({"image_url": image_url, "price": price, "description": item.description})

    return {
        "answer": result.get("answer"),
        "used_context": used_context
    }
