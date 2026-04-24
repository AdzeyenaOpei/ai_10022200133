# Kobina Opei's AI Assistant

## Project Overview

Kobina Opei's AI Assistant is an intelligent Retrieval-Augmented Generation (RAG) system developed to provide accurate, context-aware, and reliable answers from trusted institutional documents rather than relying on generic internet knowledge.

The system retrieves information from:

* Structured CSV data (Ghana Election Results)
* Unstructured PDF documents (2025 Budget Statement)

and uses Large Language Models (LLMs) to generate grounded and explainable responses.

This project was developed as part of:

**CS4241 – Introduction to Artificial Intelligence**
Academic City University
Faculty of Computational Sciences and Informatics

---

## Problem Statement

Traditional AI chatbots and general-purpose Large Language Models (LLMs) often generate hallucinated or unreliable answers because they respond without retrieving information from trusted local data sources.

This project solves that problem by implementing a custom RAG pipeline that:

* retrieves relevant information first
* uses trusted institutional documents
* reduces hallucination
* improves response accuracy
* provides explainable outputs through retrieved chunks

---

## Objectives

The project aims to:

* preprocess CSV and PDF datasets
* implement semantic chunking and retrieval
* generate embeddings using Sentence Transformers
* store vectors using FAISS
* perform Top-k similarity search
* construct prompts manually
* reduce hallucinations using prompt engineering
* build a professional Streamlit interface
* deploy the system to the cloud
* introduce a novelty feature for improved retrieval quality

---

## Datasets Used

### 1. Ghana Election Results (CSV)

Contains structured election data including:

* year
* presidential candidates
* party affiliations
* votes obtained
* winners

Used for answering election-related questions.

Example:

* Who won Ghana’s 2020 presidential election?

---

### 2. 2025 Budget Statement (PDF)

Contains financial and economic policy information such as:

* inflation targets
* GDP projections
* fiscal deficit
* tax reforms
* national budget priorities

Used for answering financial and policy-related questions.

Example:

* What is the inflation target for 2025?

---

## System Architecture

The system follows the standard RAG pipeline:

User Query
↓
Query Embedding
↓
FAISS Vector Retrieval
↓
Top-k Relevant Chunks
↓
Prompt Construction
↓
OpenAI LLM Generation
↓
Final Response

Additionally:

* retrieved chunks are shown to users
* similarity scores are logged
* responses are grounded in source documents

---

## Technology Stack

### Backend

* Python

### Frontend

* Streamlit

### Embedding Model

* sentence-transformers/all-MiniLM-L6-v2

### Vector Store

* FAISS

### LLM API

* OpenAI API

### Deployment

* Streamlit Community Cloud

### Version Control

* GitHub

---

## Project Structure

```bash id="f2m8qp"
AI/
│
├── app.py
├── build_index.py
├── requirements.txt
├── runtime.txt
├── .env
│
├── data/
│   ├── election.csv
│   └── Budget.pdf
│
├── vector_store/
│   ├── election_index.index
│   ├── budget_index.index
│   ├── election_metadata.pkl
│   └── budget_metadata.pkl
│
├── src/
│   ├── loader.py
│   ├── cleaner.py
│   ├── chunking.py
│   ├── embedding.py
│   ├── retrieval.py
│   ├── prompt.py
│   └── generator.py
│
└── README.md
```

---

## Installation Guide

### Step 1: Clone Repository

```bash id="u7p4zx"
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

---

### Step 2: Create Virtual Environment

```bash id="m3r9lv"
python -m venv venv310
```

Activate it:

### Windows

```bash id="k8v2qt"
venv310\Scripts\activate
```

### Mac/Linux

```bash id="z5n1wy"
source venv310/bin/activate
```

---

### Step 3: Install Dependencies

```bash id="q4x7mk"
pip install -r requirements.txt
```

---

### Step 4: Add OpenAI API Key

Create a `.env` file:

```env id="w9p3ra"
OPENAI_API_KEY=your_openai_api_key_here
```

---

### Step 5: Build Vector Store

```bash id="j2m6ks"
python build_index.py
```

This creates:

```text id="t7v4qn"
vector_store/
```

containing FAISS index files.

---

### Step 6: Run Application

```bash id="c5r8zp"
streamlit run app.py
```

---

## Deployment

The application is deployed using:

### Streamlit Community Cloud

Deployment includes:

* GitHub integration
* cloud hosting
* public live URL
* environment variable management
* remote access for project evaluation

### Important Deployment Requirements

* `runtime.txt` for Python version compatibility
* `requirements.txt`
* uploaded `vector_store`
* OpenAI API key in Streamlit Secrets

---

## Key Features

### Conversational Interface

A WhatsApp-style chat interface for smooth and user-friendly interaction.

---

### Retrieved Chunks Dropdown

Users can inspect the retrieved chunks used to generate answers.

This improves:

* transparency
* explainability
* trustworthiness

---

### Persistent Chat Session

Multiple questions can be asked in one session without losing context.

---

### Clear Chat Function

Allows users to reset the session easily.

---

### Direct Answer Generation

Responses are concise, accurate, and direct rather than long generic explanations.

---

## Innovation Component

### Domain-Specific Retrieval Improvement

Instead of relying only on generic semantic similarity, the system improves retrieval by prioritizing:

* election-specific queries
* winner detection
* year matching
* policy-specific financial targets
* highly relevant institutional entities

This improves answer precision significantly compared to standard retrieval.

---

## Manual Evaluation

The system was tested using manual experiment logs across both datasets.

Evaluation focused on:

* chunk relevance
* answer correctness
* hallucination reduction
* retrieval consistency
* response quality

Example test questions:

* Who won Ghana’s 2020 election?
* What is the inflation target for 2025?
* What is Ghana’s GDP growth projection?

---

## Challenges Encountered

### FAISS Deployment Issues

Cloud deployment initially failed due to:

* Python version incompatibility
* missing vector store files

Solved using:

* `runtime.txt`
* forced Git tracking of vector files

---

### Missing OpenAI Model Parameter

Resolved by explicitly specifying:

```python id="g6q1pt"
model="gpt-4o-mini"
```

---

### Prompt Hallucination

Improved through stricter prompt engineering and context restriction.

---

## Future Improvements

Possible future upgrades include:

* memory-based RAG
* user feedback loop
* hybrid retrieval (keyword + vector search)
* multi-document upload support
* admin analytics dashboard
* database scaling beyond FAISS
* institutional multi-user deployment

---

## GitHub Repository

Repository Link:

https://github.com/AdzeyenaOpei/ai_10022200133

---

## Live Deployment

Application Link:

https://yourapp.streamlit.app

---

## Author

**Kobina Opei Junior**

Academic City University
Faculty of Computational Sciences and Informatics


---

## Supervisor

Godwin N. Danso

---

## License

This project is developed strictly for academic and educational purposes.
