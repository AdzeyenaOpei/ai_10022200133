import faiss
import pickle
import numpy as np

from src.embedding import embed_query

# Load election index
election_index = faiss.read_index(
    "vector_store/election_index.index"
)

with open(
    "vector_store/election_metadata.pkl",
    "rb"
) as f:
    election_docs = pickle.load(f)

# Load budget index
budget_index = faiss.read_index(
    "vector_store/budget_index.index"
)

with open(
    "vector_store/budget_metadata.pkl",
    "rb"
) as f:
    budget_docs = pickle.load(f)


def detect_query_type(query):
    query = query.lower()

    if "who won" in query and "election" in query:
        return "election_summary"

    election_keywords = [
        "election",
        "candidate",
        "votes",
        "presidential",
        "npp",
        "ndc",
        "winner"
    ]

    for word in election_keywords:
        if word in query:
            return "election"

    return "budget"

def retrieve_documents(query, top_k=5):
    query_type = detect_query_type(query)

    #print("Detected Query Type:", query_type)

    # Automatic query expansion (internal only)
    expanded_query = query

    if query_type in ["election", "election_summary"]:
        expanded_query = (
            query +
            " Nana Akufo Addo winner total votes national result NPP NDC presidential election"
        )

    elif query_type == "budget":
        expanded_query = (
            query +
            " inflation target GDP budget fiscal policy macroeconomic target"
        )

    #print("Expanded Query:", expanded_query)

    query_vector = np.array(
        [embed_query(expanded_query)]
    ).astype("float32")

    # Route to correct FAISS index
    if query_type in ["election", "election_summary"]:
        distances, indices = election_index.search(
            query_vector,
            top_k
        )
        docs = election_docs
    else:
        distances, indices = budget_index.search(
            query_vector,
            top_k
        )
        docs = budget_docs

    results = []
    scores = []

    for idx, dist in zip(indices[0], distances[0]):
        if idx != -1:
            results.append(docs[idx])
            scores.append(float(dist))

    return results, scores