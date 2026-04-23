from src.retrieval import retrieve_documents

query = input("Ask your question: ")

docs, scores = retrieve_documents(query)

print("\nRetrieved Chunks:\n")

for i, (doc, score) in enumerate(zip(docs, scores)):
    print(f"Result {i+1}")
    print(f"Similarity Score: {score}")
    print(doc[:800])
    print("-" * 60)