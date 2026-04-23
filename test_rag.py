from src.retrieval import retrieve_documents
from src.prompt import build_prompt
from src.generator import generate_response

question = input("Ask your question: ")

# Retrieve relevant documents
docs, scores = retrieve_documents(question)

# Build final prompt
final_prompt = build_prompt(question, docs)

# Generate final answer
response = generate_response(final_prompt)

print("\nAnswer:\n")
print(response)