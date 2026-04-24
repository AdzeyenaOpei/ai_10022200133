import faiss
import pickle
import numpy as np

from src.embedding import embed_query

# ─────────────────────────────────────────────
# Load Election Index
# ─────────────────────────────────────────────
election_index = faiss.read_index(
    "vector_store/election_index.index"
)

with open(
    "vector_store/election_metadata.pkl",
    "rb"
) as f:
    election_docs = pickle.load(f)


# ─────────────────────────────────────────────
# Load Budget Index
# ─────────────────────────────────────────────
budget_index = faiss.read_index(
    "vector_store/budget_index.index"
)

with open(
    "vector_store/budget_metadata.pkl",
    "rb"
) as f:
    budget_docs = pickle.load(f)


# ─────────────────────────────────────────────
# Detect Query Type
# ─────────────────────────────────────────────
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


# ─────────────────────────────────────────────
# Retrieve Documents
# Innovation Component:
# Domain-Specific Scoring Function
# ─────────────────────────────────────────────
def retrieve_documents(query, top_k=5):
    query_type = detect_query_type(query)

    # Automatic Query Expansion + Domain-Specific Scoring
    expanded_query = query

    if query_type in ["election", "election_summary"]:
        expanded_query = query

        if "won" in query.lower():
            expanded_query += (
                " Nana Akufo Addo John Mahama winner total votes "
                "presidential election NPP NDC EC Ghana"
            )

        if "ashanti" in query.lower():
            expanded_query += (
                " Ashanti Region election regional votes"
            )

        if "volta" in query.lower():
            expanded_query += (
                " Volta Region election regional votes"
            )

        if "western" in query.lower():
            expanded_query += (
                " Western Region election regional votes"
            )

        if "bono" in query.lower():
            expanded_query += (
                " Bono East Region election regional votes"
            )

    elif query_type == "budget":
        expanded_query = query

        if "inflation" in query.lower():
            expanded_query += (
                " inflation target 2025 budget macroeconomic policy"
            )

        if "gdp" in query.lower():
            expanded_query += (
                " GDP growth projection economic growth target"
            )

        if "fiscal deficit" in query.lower():
            expanded_query += (
                " fiscal deficit target financing budget"
            )

        if "primary balance" in query.lower():
            expanded_query += (
                " primary balance target budget statement"
            )

        if "reserves" in query.lower():
            expanded_query += (
                " gross international reserves target budget statement"
            )

    # Convert query to embedding vector
    query_vector = np.array(
        [embed_query(expanded_query)]
    ).astype("float32")

    # Route query to correct FAISS index
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
