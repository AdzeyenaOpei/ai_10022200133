from rank_bm25 import BM25Okapi


def keyword_search(query, documents, top_k=3):
    tokenized_docs = [doc.split() for doc in documents]
    bm25 = BM25Okapi(tokenized_docs)

    scores = bm25.get_scores(query.split())
    ranked = sorted(zip(documents, scores), key=lambda x: x[1], reverse=True)

    return ranked[:top_k]