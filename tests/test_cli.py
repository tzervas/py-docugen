"""Tests for docugen CLI."""

import pytest
from click.testing import CliRunner
from docugen.cli import main


def test_cli_help():
    """Test that CLI shows help."""
    runner = CliRunner()
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Documentation generator" in result.output


def test_generate_command():
    """Test generate command with basic arguments."""
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create a dummy schema file
        with open("schema.yaml", "w") as f:
            f.write("project: test\nversion: '1.0.0'")

        result = runner.invoke(main, ["generate", "schema.yaml"])
        assert result.exit_code == 0
        assert "Generating documentation" in result.output