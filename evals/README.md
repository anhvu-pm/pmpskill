# PMP skill evaluation guide

This folder contains the public evaluation method and scoring rubric. Raw learner cases, personal style calibration, actual responses, scores, and reviewer notes belong under the ignored `.private/` folder. Learners only need the skill and its references to use it.

## Two evaluation modes

| Mode | Input given to the skill | Purpose |
|---|---|---|
| Primary coaching | Original question, all options, supplied answer key, and learner objection/comment | Evaluate the actual coaching response, including critical examination of the supplied key |
| Secondary independent/blind reasoning | Original question and all options only | Evaluate reasoning while hiding BOTH the answer key AND the learner objection/comment |

For every case and mode, start a separate fresh session with `skills/explain-pmp-questions/SKILL.md` and its two references loaded. Copy only the allowed fields. Keep case titles, expected answers, historical coaching, evaluator risks, and prior runs out of the input. Do not attach the complete private fixture to a blind session.

## Lightweight private workflow

1. Record the date, model/platform, and skill version or commit SHA.
2. Run the primary evaluation with all four input fields. If a live learner scenario has no supplied key, record that fact rather than inventing one.
3. Use the secondary mode as an independent baseline or targeted check when needed, in its own fresh session.
4. Save complete outputs under `.private/evals/runs/<date>/` and label their mode before scoring with [rubric.md](rubric.md). Keep scores for the two modes separate.
5. Record what helped or failed, the reviewer's corrected reply, and the reason for each important correction. Rerun when investigating a meaningful failure or inconsistency.
6. Refine the skill for demonstrated issues, then check the change against fresh scenarios. Feedback does not automatically change the skill.

## Next step: daily PMA LMS review

The maintainer will personally test and evaluate skill outputs with new real learner scenarios from PMA LMS as they arrive daily, record feedback, and refine the skill. Keep scenarios and outputs in `.private/evals/`, feedback in `.private/feedback/`, and approved examples for personal wording and tone in `.private/style/`.

The original five-case baseline and desk review have been preserved in the maintainer's local working copy under `.private/evals/baseline-2026-10-26/`. They are no longer distributed in the current public tree or included in fresh clones. Earlier public commits still contain them; ignoring or removing a file does not erase Git history.

No measured results are currently published. Public examples and aggregate findings should be deliberately reviewed for permission to share and identifying information before publication. Small samples are useful smoke tests, not estimates of population accuracy.
