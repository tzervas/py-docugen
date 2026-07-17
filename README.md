# py-docugen

<!-- FLEET-BADGES:BEGIN -->
[![CI](https://github.com/tzervas/py-docugen/actions/workflows/fleet-ci.yml/badge.svg?branch=main)](https://github.com/tzervas/py-docugen/actions/workflows/fleet-ci.yml?query=branch%3Amain)
[![Security](https://github.com/tzervas/py-docugen/actions/workflows/fleet-security.yml/badge.svg?branch=main)](https://github.com/tzervas/py-docugen/actions/workflows/fleet-security.yml?query=branch%3Amain)
<!-- FLEET-BADGES:END -->

Python documentation generator for creating comprehensive documentation from code and schemas.

## Installation

```bash
pip install py-docugen
```

## Usage

Generate documentation from schema:

```bash
docugen generate schema.yaml --output ./docs --format html
```

Validate templates:

```bash
docugen validate ./templates
```

## Development

This project uses [uv](https://github.com/astral-sh/uv) for dependency management.

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Format code
uv run black src/
uv run isort src/
```

## License

MIT License - see [LICENSE](LICENSE) for details.