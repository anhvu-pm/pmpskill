# PMP Coach evaluations

Goal: evaluate whether `explain-pmp-questions` explains disputed PMP questions accurately, independently, and helpfully.

## Assets
- `cases.md`: five original learner scenarios; supplied keys are **not** guaranteed ground truth.
- `rubric.md`: scoring instructions.
- `baseline-review.md`: initial desk review, NOT a blind execution of the skill.

## Reproducible run
1. Record model, model settings, platform, date, and skill commit SHA.
2. For each case, start a fresh session with SKILL.md and both referenced files loaded.
3. Provide question, options and learner objection ONLY; hide supplied key, historical answer and case-specific risk.
4. Save output verbatim to `evals/runs/<date>/<case>-<trial>.md`.
5. Score against rubric after response is frozen; log which answers are disputed.
6. Repeat each case three times (15 total). Compare decisions and uncertainty handling across runs.
7. Review failures, fix only demonstrated defects, rerun same cases.

Private beta gate: mean >=85/100; no critical failures; >=90% consistency across repeated decisions. Five questions are an engineering smoke test, not an estimate of population accuracy.
