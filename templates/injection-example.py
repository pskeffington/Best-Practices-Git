from best_practices_git.claims import ClaimLevel

# Planned injectable use pattern:
#
# from best_practices_git.inject import WorkflowRun
#
# with WorkflowRun("model-validation") as run:
#     metrics = evaluate_model(model, X_test, y_test)
#     run.log_metric("auc", metrics["auc"])
#     run.log_artifact("artifacts/results/result-bundle.md")
#     run.register_claim(
#         text="The model improved over baseline performance in internal validation.",
#         level=ClaimLevel.COMPARATIVE,
#         evidence_path="artifacts/results/result-bundle.md",
#         evidence_description="Baseline and candidate model comparison",
#         boundary_note="External validation is required before generalization.",
#     )
