def build_prompt(query, docs):
    ranked_context = "\n\n".join([str(doc) for doc in docs[:5]])

    prompt = f"""
You are an Academic City University AI assistant.

RULES:
1. Use ONLY the provided context.
2. Give a direct final answer.
3. Keep the answer short (maximum 2 sentences).
4. Do NOT provide step-by-step explanation.
5. For election winner questions, compare the candidates and choose the most likely national winner based on the strongest overall evidence from the retrieved regions.
6. If one candidate appears stronger across multiple major regions, state that candidate clearly.

CONTEXT:
{ranked_context}

QUESTION:
{query}

FINAL ANSWER:
"""

    return prompt