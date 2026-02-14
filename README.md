# 🏎️ Supercar Intelligence Platform

**Hybrid Data Intelligence for Automotive Insights and Performance**

---

## 🎯 Objective

This project demonstrates a **hybrid automotive intelligence platform**, combining:

- Structured data (specs, performance, price)  
- Unstructured data (reviews, historical descriptions)  
- Hybrid querying (SQL + RAG)  
- **Production-ready API** with FastAPI  

The goal is not dashboards, but a **clean, scalable, and testable architecture** showcasing technical decision-making and platform-level thinking.

---

## 🗂️ Data Layers (Lakehouse)

| Layer | Description |
|-------|-------------|
| **RAW** | Raw data: CSV, JSON, supercar reviews |
| **Bronze** | Cleaning, deduplication, handling missing or inconsistent data |
| **Silver** | Standardization, type casting, segmentation into chunks for RAG |
| **Gold** | Query-ready data, derived metrics, and generated embeddings |

Tools: **dbt + Databricks Free Tier**  

---

## 🧠 Semantic Pipeline (RAG)

1. Text chunked (~500 words per chunk)  
2. Embedding generation:
   - **OpenAI embeddings** (free credits) **or**
   - **Open-source local LLM** (`text-embedding-3-small`, `ggml`)  
3. Vector indexing with **FAISS local**
4. Top-k context retrieval
5. Contextualized answer generation with LLM

---

## ⚡ Query Router (Heuristic)

The **Query Router** dynamically determines the execution path:

| Question Type | Strategy |
|---------------|----------|
| Structured | SQL via Gold tables (e.g., top speed, horsepower) |
| Semantic | RAG + embeddings |
| Hybrid | SQL filters a subset → RAG applies context |

**Reasoning:**  
- Deterministic → testable and predictable  
- Reduces cost (avoids unnecessary LLM calls)  
- Demonstrates professional architecture and technical maturity  

---

## 🛠 Tech Stack

| Component | Technology | Role |
|-----------|-----------|------|
| Data Processing & Modeling | **Databricks Free Tier + dbt** | Lakehouse, transformation layers, versioning |
| Backend & API | **FastAPI + Pydantic** | Modular, typed, production-ready API |
| Vector Storage | **FAISS (local)** | Embedding storage without cost |
| LLM & Embeddings | **OpenAI** (or **local open-source LLM**) | Contextualized answers and embeddings |
| Text Processing | **NLTK / spaCy** | Light cleaning and tokenization |
| Testing | **pytest** | Unit tests for router, pipelines, API |
| Orchestration | **Databricks Jobs + GitHub Actions** | Incremental execution and pipeline scheduling |
| Utilities | **python-dotenv, logging** | Environment management and structured logs |

---

## 💡 Technology Rationale

- **FastAPI** → Professional, modular, typed backend  
- **FAISS local** → Zero cost, fast, sufficient for portfolio projects  
- **Heuristic Query Router** → Deterministic, testable, reduces LLM usage  
- **OpenAI or local LLM** → Flexibility for cost-free development  
- **Databricks + dbt** → Professional Lakehouse architecture with versioning and tests  
- **Python** → Backbone of the pipeline (ingestion, embeddings, RAG, API, testing)  

---

## 💰 Zero-Cost Development Strategy

1. **Embeddings and LLM**  
   - Generate embeddings **once** and store locally (FAISS / JSON / Delta)  
   - User questions → only generate LLM responses as needed  
   - Optionally use **local open-source LLM** (`ggml`) to eliminate API costs entirely  

2. **Infrastructure**  
   - **FAISS local** → zero cost  
   - **Databricks Free Tier** → run clusters only when needed  

3. **Backend**  
   - **FastAPI + Uvicorn** → open-source  
   - Unit testing → pytest → zero cost  

4. **CI/CD**  
   - **GitHub Actions** → free plan sufficient for small pipelines  

---

## 🧩 Project Structure
app/
├── main.py
├── routers/
├── services/
├── schemas/
├── core/
pipelines/
├── ingestion/
├── embeddings/
rag/
tests/
dbt/
data/
docs/
requirements.txt
Dockerfile
README.md

---

## 🚀 Development Workflow

1. Ingest RAW data (CSV/JSON from Kaggle)  
2. Transform and normalize (Bronze → Silver → Gold)  
3. Generate embeddings and build vector index (FAISS local)  
4. Configure heuristic Query Router  
5. Expose `/ask` endpoint via FastAPI  
6. Unit testing, structured logs, and auditing  
7. Deploy locally or via Databricks Free Tier  

**Future Enhancements:**  
- Hybrid or LLM-assisted routing for ambiguous questions  
- Pinecone for industrial-scale vector storage  
- Advanced local open-source models for improved answer quality  

---

## 🔮 Conclusion

This project demonstrates **data engineering + RAG + LLM + production-ready API** in a **hybrid, modular, testable, zero-cost workflow**, showcasing strong technical design and platform-level thinking.
