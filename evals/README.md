# PMP Coach evaluations

Goal: evaluate whether `explain-pmp-questions` explains disputed PMP questions accurately, independently, and helpfully.

## Assets
- `cases.md`: five original learner scenarios; supplied keys are **not** guaranteed ground truth.
- `rubric.md`: scoring instructions.
- `baseline-review.md`: initial desk review, NOT a blind execution of the skill.

## Lightweight evaluation workflow
1. Record the date, model/platform, and skill commit SHA.
2. For each case and each evaluation mode, start a separate fresh session with `SKILL.md` and both referenced files loaded. Do not reuse the primary conversation for the blind run or provide the full evaluator fixture.
3. Run the **primary coaching evaluation** with the original question, all options, supplied answer key, and learner objection/comment. This tests the real coaching task: respond to the learner while evaluating the key critically rather than treating it as ground truth.
4. Run the **secondary independent/blind reasoning evaluation** with the question and all options only. Hide both the supplied answer key and the learner objection/comment, along with the historical answer and case-specific risk.
5. Save each output verbatim under `evals/runs/<date>/`, label it `primary` or `blind`, then score the frozen output with `rubric.md`. Keep results for the two modes separate.
6. Rerun only when investigating an unclear, inconsistent, or failed result. Record feedback and refine the skill only for demonstrated issues.

The five fixtures are a lightweight engineering smoke test, not an estimate of population accuracy. The supplied keys are evidence to examine in the primary evaluation, not unquestionable ground truth.

## Next step: real learner scenarios
The user will personally test and evaluate the skill outputs with new real learner scenarios from the PMA LMS as they arrive daily. They will record feedback and use the findings to refine the skill. Keep this loop lightweight: capture the scenario and output, note what helped or failed, and make focused refinements when a pattern or material issue appears.

Private beta gate: mean >=85/100 and no critical failures. Check consistency with targeted reruns when a decision is unclear or unstable.

## Personal coaching pilot
Use the actual skill with the original question, all options, supplied key (when available), and the learner's comment. Suggested prompt:

> Use $explain-pmp-questions to draft a reply to this learner in brief Vietnamese. Evaluate the supplied key critically, address the learner's objection, and follow the coaching style in the skill. I will review the reply before using it.

Keep one short feedback note per scenario: date/case, skill version, draft, your corrected reply, and why you changed it. A few approved replies can help calibrate your personal wording and tone. Feedback does not automatically update the skill; incorporate recurring findings deliberately, then try them on new scenarios.

The current skill specifies a coaching style, but no saved executions yet demonstrate answer quality or fidelity to the user's personal style. This is ready for a personally reviewed pilot; measured results will come from the baseline and daily PMA LMS feedback.
