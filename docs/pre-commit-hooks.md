# Pre-commits Hooks

We use [pre-commit](https://pre-commit.com/).

The list of hooks installed by default is inspired by [`Ty`'s repo](https://github.com/astral-sh/ty/blob/main/.pre-commit-config.yaml)

💡 Some hooks are disabled by default (like `actionlint`) because they are slow. To trigger all hooks manually, you can run `pre-commit run -a --hook-stage=manual`, or `pre-commit run -a actionlint --hook-stage=manual` to run only the hook called `actionlint`.

## Definitive List

- `Ruff` lint and formatting
- `uv` lock check
- `Gitleaks`
- `Basedpyright`

Most others might be dropped later.

## Incoming

- [Code embedder](https://github.com/kvankova/code-embedder/tree/v1.1.1/)
- REPL Snippets (currently only a script)

## Tried and Dropped

- [trufflehog](https://github.com/trufflesecurity/trufflehog)
  - Doesn't seem to work well on local files, we might try as github action

- [pyproject-fmt](https://github.com/tox-dev/pyproject-fm)
  - Weird formatting and bad documentation
