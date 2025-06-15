# Pre-commits Hooks

Most are inspired by [`Ty`'s repo](https://github.com/astral-sh/ty/blob/main/.pre-commit-config.yaml)

## Default List

- `Ruff` lint and formatting
- `uv` lock check
- `Gitleaks`
- `Basedpyright`

## Need Config/Testing

- <https://github.com/igorshubovych/markdownlint-cli>

## Tried and Dropped

- [trufflehog](https://github.com/trufflesecurity/trufflehog)
  - Doesn't seem to work well on local files, we might try as github action

- [pyproject-fmt](https://github.com/tox-dev/pyproject-fm)
  - Weird formatting and bad documentation
