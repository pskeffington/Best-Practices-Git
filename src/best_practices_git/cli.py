"""Command-line interface for the query-to-publication workflow."""

import subprocess
from argparse import ArgumentParser
from pathlib import Path

from .audit import build_audit_report
from .pipeline import default_pipeline
from .standards import default_mappings
from .verification import PipelineVerifier


class WorkflowCommand:
    """Executable workflow command for creating manuscript artifacts."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.pipeline = default_pipeline()

    def render_templates(self) -> None:
        """Create artifact templates for every pipeline stage."""
        self.pipeline.write_artifact_templates(self.root)

    def print_status(self) -> None:
        """Print the default workflow status."""
        for stage in self.pipeline.stages:
            percent = int(stage.completion_ratio * 100)
            print(f"{stage.name}: {percent}% complete")
            missing = stage.missing_fields()
            if missing:
                print("  missing: " + ", ".join(missing))

    def current_git_ref(self) -> str:
        """Return the current Git commit hash, if available."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
            )
        except (OSError, subprocess.CalledProcessError):
            return "unknown"
        return result.stdout.strip() or "unknown"

    def write_audit_report(self) -> tuple[Path, Path, Path, Path]:
        """Run verification and write repeatable audit reports."""
        verifier = PipelineVerifier(
            pipeline=self.pipeline,
            mappings=default_mappings(),
        )
        report = build_audit_report(
            verifier.run_all(),
            git_ref=self.current_git_ref(),
        )
        audit_dir = self.root / "artifacts" / "audits"
        return report.write_outputs(audit_dir)


def build_parser() -> ArgumentParser:
    """Build the CLI parser."""
    parser = ArgumentParser(description="Manage the manuscript workflow scaffold.")
    parser.add_argument(
        "command",
        choices=("audit", "init-artifacts", "status"),
        help="Workflow command to run.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root where artifacts should be written.",
    )
    return parser


def main() -> None:
    """Run the CLI."""
    args = build_parser().parse_args()
    command = WorkflowCommand(root=Path(args.root))

    if args.command == "audit":
        outputs = command.write_audit_report()
        print("Wrote audit reports:")
        for output_path in outputs:
            print(f"- {output_path}")
        return

    if args.command == "init-artifacts":
        command.render_templates()
        return

    if args.command == "status":
        command.print_status()
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
