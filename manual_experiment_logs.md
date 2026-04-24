# Manual Experiment Logs

This section presents the manual testing carried out on Kobina Opei's AI Assistant to evaluate retrieval relevance, response accuracy, hallucination control, and overall system performance.

The tests were conducted using both:

* Ghana Election Results (CSV)
* 2025 Budget Statement (PDF)

The goal was to verify whether the system retrieves relevant chunks and produces correct final answers grounded in the provided documents.

---

| Test No. | Question Asked                                               | Retrieved Chunk Relevant? | Final Answer Correct? | Observation                                                                                                         |
| -------- | ------------------------------------------------------------ | ------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1        | Who won Ghana’s 2020 presidential election?                  | Yes                       | Yes                   | Query expansion improved retrieval across multiple regions and produced the correct final answer (Nana Akufo-Addo). |
| 2        | What is the inflation target for 2025?                       | Yes                       | Yes                   | Retrieved PDF chunks directly contained the inflation target of 15.0%.                                              |
| 3        | What is Ghana’s projected GDP growth for 2025?               | Yes                       | Yes                   | Correct chunk found in budget document showing GDP growth projection.                                               |
| 4        | Which party had the highest votes in Ashanti Region in 2020? | Yes                       | Yes                   | Election CSV retrieval was accurate and final response matched expected result.                                     |
| 5        | What is the fiscal deficit target for 2025?                  | Yes                       | Yes                   | Relevant PDF chunk retrieved successfully with exact fiscal deficit percentage.                                     |
| 6        | Who won the Western Region in the 2020 election?             | Yes                       | Yes                   | Retrieved chunk clearly showed Nana Akufo-Addo with higher votes than John Mahama.                                  |
| 7        | What is the primary balance target for 2025?                 | Yes                       | Yes                   | Budget document retrieval was correct and response was precise.                                                     |
| 8        | What was the inflation target for 2024?                      | Yes                       | Yes                   | Historical macroeconomic target retrieved correctly from PDF.                                                       |
| 9        | Which candidate won the Volta Region in 2020?                | Yes                       | Yes                   | System correctly identified John Dramani Mahama based on retrieved chunks.                                          |
| 10       | What is Ghana’s gross international reserves target?         | Partially                 | Yes                   | Correct answer generated after considering multiple top chunks instead of only one.                                 |
| 11       | What is the non-oil GDP growth target for 2025?              | Yes                       | Yes                   | PDF chunk was highly relevant and final answer was accurate.                                                        |
| 12       | Who had the highest votes in Bono East Region in 2020?       | Yes                       | Yes                   | Election data correctly identified the leading candidate from retrieved CSV rows.                                   |
| 13       | What tax reforms were introduced in the 2025 budget?         | Partially                 | Partially             | Broad query retrieved useful chunks but final answer lacked full detail.                                            |
| 14       | Which independent candidate had the highest votes in 2020?   | No                        | No                    | Retrieval focused on major parties and failed to rank independent candidates effectively.                           |
| 15       | Compare inflation targets for 2024 and 2025                  | Yes                       | Yes                   | System successfully compared both years using multiple PDF chunks and generated correct summary.                    |

---

## Summary of Evaluation

### Successful Retrieval Cases

Most direct factual questions such as election winners, inflation targets, GDP projections, and fiscal targets achieved high retrieval relevance and correct final responses.

This demonstrates strong system performance for:

* structured election data queries
* exact financial target questions
* year-specific comparisons

---

### Partial Retrieval Cases

Broad or comparative questions such as tax reforms and reserves target required multiple chunks before accurate answers were produced.

This revealed the importance of:

* Top-k retrieval
* query expansion
* domain-specific relevance ranking

---

### Failure Cases

Questions involving:

* independent candidates
* uncommon entities
* broad policy summaries

sometimes produced weak retrieval results due to semantic bias toward dominant entities like NPP and NDC.

This motivated the implementation of:

## Query Expansion

as the innovation component to improve retrieval precision.

---

## Conclusion from Testing

The manual experiments confirm that Kobina Opei's AI Assistant performs strongly for high-value institutional queries while maintaining transparency through retrieved chunk display.

The system successfully reduces hallucination by grounding answers in trusted source documents rather than relying on unsupported LLM generation.
