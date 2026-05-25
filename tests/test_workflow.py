from best_practices_git import ManuscriptStage, ManuscriptWorkflow


def test_workflow_advances_stage():
    workflow = ManuscriptWorkflow(title="From Query to Publication")
    advanced = workflow.advance_to(ManuscriptStage.MANUSCRIPT)

    assert workflow.stage == ManuscriptStage.QUERY
    assert advanced.stage == ManuscriptStage.MANUSCRIPT


def test_workflow_completes_gate_once():
    workflow = ManuscriptWorkflow(title="From Query to Publication")
    updated = workflow.complete_gate("query framed").complete_gate("query framed")

    assert updated.completed_gates == ("query framed",)
