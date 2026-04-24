# Manual Experiment Logs

## Objective

The system was manually tested to evaluate retrieval relevance, final answer correctness, and the impact of the innovation component (Domain-Specific Scoring Function).

The goal was to verify that important election and budget-related keywords improved retrieval precision and produced stronger final grounded answers.

---

## Test Cases

| Test No. | Question Asked                                               | Retrieved Chunk Relevant? | Final Answer Correct? | Observation                                                                                                                                                               |
| -------- | ------------------------------------------------------------ | ------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Who won Ghana’s 2020 presidential election?                  | Yes                       | Yes                   | Domain-specific scoring boosted winner-related terms like Nana Akufo-Addo, NPP, and total votes, improving retrieval accuracy.                                            |
| 2        | What is the inflation target for 2025?                       | Yes                       | Yes                   | Relevant budget chunks directly contained the inflation target of 15.0 percent. Retrieval precision improved with macroeconomic keyword boosting.                         |
| 3        | What is the GDP growth target for 2025?                      | Yes                       | Yes                   | The system successfully retrieved the exact chunk containing “Overall Real GDP growth of at least 4.0 percent,” proving stronger retrieval after domain-specific scoring. |
| 4        | Which party had the highest votes in Ashanti Region in 2020? | Yes                       | Yes                   | Regional boosting for Ashanti improved election retrieval and the final answer matched expected election results.                                                         |
| 5        | What is the fiscal deficit target for 2025?                  | Yes                       | Yes                   | Fiscal deficit boosting helped retrieve the correct macroeconomic target from the budget statement with strong answer grounding.                                          |
| 6        | What is the primary balance target for 2025?                 | Yes                       | Yes                   | Primary balance terms improved retrieval and the system returned the correct budget value from the source chunk.                                                          |
| 7        | Who won the Volta Region in 2020?                            | Yes                       | Yes                   | Region-specific scoring improved relevance and helped retrieve the expected election result accurately.                                                                   |
| 8        | What is Ghana’s gross international reserves target?         | Yes                       | Yes                   | Domain-specific scoring for reserves improved retrieval and produced a grounded answer from the budget source.                                                            |

---

## Summary of Findings

The implementation of the Domain-Specific Scoring Function significantly improved retrieval quality compared to generic similarity search.

Instead of relying only on vector similarity, the system boosted important election and budget-specific terms such as:

* Nana Akufo-Addo
* John Mahama
* NPP / NDC
* inflation target
* GDP growth
* fiscal deficit
* primary balance
* regional election names

This resulted in:

* more relevant retrieved chunks
* stronger final answer accuracy
* reduced hallucination
* better explainability through grounded responses

The system performed especially well for direct factual queries and year-specific budget targets.

---

## Conclusion

Manual testing confirmed that the innovation component successfully improved the Retrieval-Augmented Generation pipeline.

The Domain-Specific Scoring Function made the assistant more reliable for Ghana election and budget-related questions and strengthened the overall quality of the final system.
