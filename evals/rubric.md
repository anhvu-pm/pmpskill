# Evaluation rubric

Each dimension receives 0–4 points. Weighted score is (score/4) × weight.

| Dimension | Weight | Excellent (4/4) |
|---|---:|---|
| Answer defensibility | 30 | Chooses most defensible answer or explicitly flags ambiguity independent of supplied key |
| Situational reasoning | 25 | Uses decisive facts, status, authority, constraints, FIRST/NEXT |
| Option comparison | 20 | Primary: directly handles learner's strongest alternative; blind: compares the strongest competing option from the question |
| Principle accuracy and transfer | 15 | Relevant bounded rule, not an absolute keyword heuristic |
| Coaching clarity | 10 | Concise helpful Vietnamese, no invented context |

Critical failure: confidently defends a doubtful key with unsound logic, invents decisive facts, makes a serious safety/compliance error, or presents an incorrect universal principle.

Case-specific hazards and expected-answer notes belong with the private fixtures under `.private/evals/`. Keep them out of the model's input.

Record actual response, score per dimension, critical failures, uncertainty, and evaluator notes under `.private/evals/`. Do not treat the supplied exam answer key as unquestionable ground truth.

Apply the same rubric to both modes, but interpret the evidence in context:

- **Primary coaching:** assess whether the response directly addresses the learner's objection/comment and evaluates the supplied key critically.
- **Secondary independent/blind reasoning:** assess the answer and reasoning without expecting a response to an objection that was intentionally hidden.
