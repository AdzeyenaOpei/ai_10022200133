import os
import faiss
import pickle
import numpy as np

from src.loader import load_csv, load_pdf
from src.cleaner import clean_csv, clean_text
from src.chunking import chunk_text
from src.embedding import embed_chunks

os.makedirs("vector_store", exist_ok=True)

print("Loading files...")

# Load CSV
csv_data = load_csv("data/election.csv")
csv_data = clean_csv(csv_data)

# Convert CSV rows into meaningful text
csv_rows = []

for _, row in csv_data.iterrows():
    sentence = " | ".join(
        [f"{col}: {row[col]}" for col in csv_data.columns]
    )
    csv_rows.append(sentence)

csv_text = "\n".join(csv_rows)

# Load PDF
pdf_text = load_pdf("data/Budget.pdf")
pdf_text = clean_text(pdf_text)

print("Chunking...")

# Separate chunking
csv_chunks = chunk_text(csv_text)
pdf_chunks = chunk_text(pdf_text)

print("Embedding...")

# Create embeddings separately
csv_embeddings = embed_chunks(csv_chunks)
pdf_embeddings = embed_chunks(pdf_chunks)

csv_embeddings = np.array(csv_embeddings).astype("float32")
pdf_embeddings = np.array(pdf_embeddings).astype("float32")

print("Creating FAISS indexes...")

# Create separate indexes
election_index = faiss.IndexFlatL2(csv_embeddings.shape[1])
budget_index = faiss.IndexFlatL2(pdf_embeddings.shape[1])

election_index.add(csv_embeddings)
budget_index.add(pdf_embeddings)

# Save indexes
faiss.write_index(
    election_index,
    "vector_store/election_index.index"
)

faiss.write_index(
    budget_index,
    "vector_store/budget_index.index"
)

# Save metadata separately
with open("vector_store/election_metadata.pkl", "wb") as f:
    pickle.dump(csv_chunks, f)

with open("vector_store/budget_metadata.pkl", "wb") as f:
    pickle.dump(pdf_chunks, f)

print("FAISS indexes created successfully")