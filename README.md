<p align="center">
    <em>SnakeForge, the opinionated Python template that gives you what you need, and no more.</em>
</p>

# Your favorite template for Python projects 🐍

## ✨ Features

- `GitHub` hosted repo and CI/CD workflows for
- `uv` managed dependencies and virtual environment
- Strict `Ruff` linting and formatting
- Static type testing with `ty`, yes we love [astral](https://astral.sh/)
- [`pre-commit hooks`](/docs/pre-commit-hooks.md) checking all this
- [GitHub Actions](/docs/github-action.md) CI/CD workflows
- [Versioning](/docs/versioning.md) with `Commitizen`
- Dynamic project metadata with `hatch` and `hatchling` build backend
- `Markdown` documentation inspired by [FastAPI](https://fastapi.tiangolo.com/) and [Typer](https://typer.tiangolo.com/)

## Contents <!-- omit from toc -->

- [✨ Features](#-features)
- [📋 Requirements](#-requirements)
- [🚀 Quickstart](#-quickstart)
  - [Roadmap](#roadmap)
- [Advanced Usage](#advanced-usage)
  - [Update your project](#update-your-project)
- [Resources](#resources)

## 📋 Requirements

Unsure the following dependencies are installed:

- Python>=3.12
- [Copier](https://copier.readthedocs.io/en/stable/) with [copier_templates_extensions](https://github.com/copier-org/copier-templates-extensions)
- [Git](https://git-scm.com/downloads)
- [GitHub CLI (gh)](https://cli.github.com/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## 🚀 Quickstart

1. **Install the [requirement](#-requirements)**

    You can verify all required tools are correctly installed by running:

    ```shell
    copier --version
    git --version
    gh --version
    uv --version
    ```

2. **Generate the Python project:**

   TODO

3. **Setup the project**

    Follow the instructions displayed at the end of the generation process to initialize Git, create the GitHub repository, and set up the virtual environment

4. **Start coding your awesome package!**

💡 Most of the time, if you want to update something that depends on an answer from the template (e.g., min python version, project description, etc), you better update the template with then new value so that it changes the value everywhere automatically.

### Roadmap

- add license classifiers in `pyproject.tom`
- Replace `hatch` with `uv` (when the build backend is feature complete)
- use `ty` as type checker, yes we love [astral.sh](https://astral.sh/) stuff..!
- us devcontainer
- docs template with mkdocs, also check [mdbook](https://rust-lang.github.io/mdBook/)
- issue template
- docker setup
- app vs package
- typedsettings and cyclopts with examples
- pypi
- [Changelog](https://keepachangelog.com/en/1.1.0/)
- Add proper testing with [this](https://github.com/KyleKing/copier-template-tester/tree/main/docs)
- Add profiles like [this](https://github.com/NLeSC/python-**template**)
- Add proper messages
- Replace `uv-dynamic-version` with the features from [commitizen](https://github.com/commitizen-tools/commitizen) (and also changelog)
- code embbedder and print result embedder in precommit hook
- Replace plain tasks by some more practical task runner (invoke, etc)
- Clean up template formatting (toml, etc)

## Advanced Usage

If you use this template often, try using [copier settings](https://copier.readthedocs.io/en/stable/settings/) to save time during the setup!

### Update your project

TODO

## Resources

Check: <https://blog.dusktreader.dev/2025/04/06/bootstrapping-python-projects-with-copier/#automating-github-deployment-with-tasks>

Based on

- <https://github.com/serious-scaffold/ss-python/tree/main>
- <https://github.com/audreyfeldroy/cookiecutter-pypackage>
- <https://github.com/DiamondLightSource/python-copier-template>
