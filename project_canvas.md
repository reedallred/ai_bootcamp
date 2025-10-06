# Capstone Project Plan: AI-Powered Amazon Product Assistant

## Problem Statement

Online shoppers often struggle to make informed purchasing decisions due to the overwhelming amount of product information and reviews on Amazon. Manually reading and comparing products can be time-consuming and inefficient. The goal of this project is to develop an **AI-powered Amazon product assistant** that can understand user queries, retrieve relevant product information, summarize customer opinions, and make intelligent recommendations — evolving from a basic Q&A chatbot into a **multi-step, agentic AI system** capable of autonomous reasoning and task execution.

---

## Data Knowledge

- **Data Sources:**  
  - Publicly available Amazon product data, such as the **Amazon Product Reviews** and **Metadata datasets** (e.g., titles, descriptions, categories, and user reviews).  
  - These datasets are rich in unstructured text, making them ideal for building a language-model-powered assistant.  

- **Data Preparation:**  
  - A **filtered subset** (e.g., products from one or two categories) will be used for efficient prototyping.  
  - Data will be **cleaned, tokenized, and indexed** for efficient retrieval.  
  - Vector embeddings will be generated for use in **Retrieval-Augmented Generation (RAG)** workflows.  

---

## Performance & Metrics & Rules

- **Core Metrics:**  
  - **Accuracy / Relevance:** How well the assistant retrieves and answers product-related questions.  
  - **Response Coherence:** Measured by user or peer evaluation (fluency, factual consistency).  
  - **User Satisfaction:** Based on interaction logs or survey feedback.  
  - **Latency:** Average time per query response.  

- **Project Rules & Constraints:**  
  - Only **public, non-proprietary data** will be used.  
  - The model will not provide unverifiable claims or hallucinations about products.  
  - Each sprint must deliver a **working, testable system increment** aligned with the bootcamp’s objectives.  

---

## Resources & Stakeholders

- **Resources:**  
  - Computing environment: Python, Jupyter Notebooks, cloud GPU/CPU instances.  
  - Frameworks: LangChain, LlamaIndex, Hugging Face Transformers, or OpenAI API for LLM integration.  
  - Vector database: FAISS, Chroma, or Pinecone for retrieval.  
  - Deployment tools: Streamlit, Gradio, or FastAPI for app interface.  

- **Stakeholders:**  
  - **Bootcamp Participants:** Developers building and testing system features weekly.  
  - **Instructors/Mentors:** Provide guidance, code reviews, and feedback.  
  - **End Users:** Consumers who will interact with the final AI assistant for product discovery and comparison.  

---

## Risk & Mitigation

| **Risk** | **Impact** | **Mitigation Strategy** |
|-----------|-------------|--------------------------|
| Data quality issues (e.g., missing fields, inconsistent formats) | Medium | Perform early data cleaning and validation scripts |
| Model hallucinations or irrelevant answers | High | Use RAG and rule-based post-processing to anchor responses in retrieved data |
| API cost overruns or limited compute | Medium | Use open-source models and local embeddings when possible |
| Feature creep or missed deadlines | High | Stick to weekly sprint deliverables and scope limits |
| Deployment errors or integration issues | Medium | Use CI/CD pipelines and incremental deployment testing |

---

## Deployment & Integration

- **Environment:** Containerized deployment using Docker or cloud services (e.g., AWS, GCP, or Render).  
- **Integration:**  
  - Backend integrates vector database, LLM API, and data retrieval pipeline.  
  - Frontend (web or chat UI) connects through REST or WebSocket endpoints.  
  - Continuous integration for model updates and retraining.  
- **Testing:**  
  - Unit and integration tests for each pipeline stage.  
  - User acceptance testing during final sprint.  

---

## AI Approach & Methodology

1. **Week 1–2: Foundational RAG System**  
   - Implement data ingestion, embedding creation, and retrieval pipeline.  
   - Build a Q&A chatbot that answers using retrieved context.  

2. **Week 3–4: Contextual Understanding & Summarization**  
   - Add summarization of customer reviews and comparison features.  
   - Improve grounding and factual consistency.  

3. **Week 5–6: Agentic Capabilities**  
   - Integrate tool use and reasoning chains (multi-step workflows).  
   - Enable actions like “find top-rated laptops under $1000” or “compare two products.”  

4. **Week 7–8: Optimization & Deployment**  
   - Performance tuning, caching, and user interface improvements.  
   - Final deployment as a production-ready AI assistant.  

---

## Timelines & Milestones

| **Week** | **Milestone** | **Deliverable** |
|-----------|----------------|----------------|
| Week 1 | Project setup & dataset preparation | Cleaned and indexed product subset |
| Week 2 | RAG implementation | Basic Q&A chatbot with retrieval |
| Week 3 | Review summarization & recommendation logic | Enhanced assistant responses |
| Week 4 | Evaluation framework | Metrics tracking and error analysis tools |
| Week 5 | Multi-step agent reasoning | Assistant can perform reasoning tasks |
| Week 6 | Tool integration | External API or data lookup tools added |
| Week 7 | Frontend + backend integration | Full user interface and deployment |
| Week 8 | Final presentation & demo | Production-ready AI assistant |
