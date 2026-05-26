"""Command-line interface for the query-to-publication workflow."""

from argparse import ArgumentParser
from pathlib import Path

from .pipeline import default_pipeline


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


def build_parser() -> ArgumentParser:
    """Build the CLI parser."""
    parser = ArgumentParser(description="Manage the manuscript workflow scaffold.")
    parser.add_argument(
        "command",
        choices=("init-artifacts", "status"),
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

    if args.command == "init-artifacts":
        command.render_templates()
        return

    if args.command == "status":
        command.print_status()
        return

    raise ValueError(f"Unsupported command: {args.command}")


if __name__ == "__main__":
    main()
