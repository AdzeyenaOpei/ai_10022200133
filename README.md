# Kobina Opei's AI Assistant

## Academic City University RAG Project

Kobina Opei's AI Assistant is a Retrieval-Augmented Generation (RAG) system built for Academic City University to provide intelligent answers from trusted institutional documents.

The system allows users to query:

* Ghana 2020 Presidential Election Results (CSV)
* 2025 Ghana Budget Statement (PDF)

Instead of relying on general AI responses, the application retrieves relevant document chunks using vector search (FAISS) and generates grounded responses using OpenAI.

---

## Project Objectives

The goal of this project is to:

* Reduce manual searching through large documents
* Improve decision-making using trusted source documents
* Minimize hallucination in AI-generated responses
* Provide transparent answers by showing retrieved chunks
* Demonstrate practical Retrieval-Augmented Generation (RAG)

---

## Key Features

### Query Input

Users can ask natural language questions such as:

* Who won Ghana’s 2020 presidential election?
* What is the inflation target for 2025?
* What is the GDP growth target for 2025?
* What is the fiscal deficit target?

### Retrieved Chunk Display

The system displays the exact document chunks used to generate the final answer.

This improves:

* transparency
* trust
* explainability
* retrieval validation

### Final AI Response

After retrieval, the system generates a final grounded answer using OpenAI.

### Persistent Chat Interface

The application maintains conversation history for a smooth user experience.

---

## Innovation Component (Part G)

### Domain-Specific Scoring Function

A domain-specific scoring mechanism was introduced to improve retrieval precision.

Instead of using generic similarity search only, the system boosts important election and budget-related terms such as:

* Nana Akufo-Addo
  n- John Mahama
* NPP / NDC
* inflation target
* GDP growth
* fiscal deficit
* primary balance
* regional election names

This improves:

* chunk relevance
* answer accuracy
* retrieval precision
* hallucination reduction

### Example

User query:

`What is the GDP growth target for 2025?`

The system strengthens retrieval using terms like:

`GDP growth projection economic growth target budget macroeconomic policy`

This helps FAISS retrieve stronger supporting chunks.

---

## Technologies Used

### Frontend

* Streamlit

### Retrieval Layer

* FAISS (Vector Search)
* Sentence Transformers
* NumPy

### Generation Layer

* OpenAI API

### Data Processing

* Pandas
* PyPDF
* Python Dotenv

---

## Project Structure

```text
AI/
│
├── app.py
├── build_index.py
├── requirements.txt
├── runtime.txt
├── README.md
├── manual_experiment_logs.md
│
├── data/
│   ├── election.csv
│   └── budget.pdf
│
├── src/
│   ├── retrieval.py
│   ├── generator.py
│   ├── prompt.py
│   └── embedding.py
│
├── vector_store/
│   ├── election_index.index
│   ├── election_metadata.pkl
│   ├── budget_index.index
│   └── budget_metadata.pkl
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/AdzeyenaOpei/ai_10022200133.git
cd ai_10022200133
```

### Create Virtual Environment

```bash
python -m venv venv310
```

### Activate Virtual Environment

#### Windows

```bash
.\venv310\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Deployment

The application is deployed to the cloud for public access using Render / Streamlit hosting.

This allows:

* remote access
* live demonstration
* investor presentation
* lecturer evaluation

---

## Manual Experiment Logs

Manual testing was performed using multiple factual and comparative queries to evaluate:

* retrieval relevance
* final answer correctness
* chunk quality
* hallucination control

Examples tested include:

* inflation target for 2025
* GDP growth target
* election winners by region
* fiscal deficit target
* primary balance target

Results showed strong performance for direct factual queries and improved retrieval quality after implementing domain-specific scoring.

---

## Author

### Kobina Opei

Academic City University

Introduction to Artificial Intelligence Project

RAG-Based Intelligent Assistant System

---

## Final Note

This project demonstrates how Retrieval-Augmented Generation can be applied to real institutional decision-making problems by combining vector search, document grounding, and large language models into a reliable AI assistant.
