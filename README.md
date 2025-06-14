<p align="center">
    <em>SnakeForge, the opinionated Python template that gives you what you need, and no more.</em>
</p>

# Your favorite template for Python projects 🐍

## ✨ Features

- `GitHub` hosted repo and CI/CD workflows for
- `uv` managed dependencies and virtual environment
- Strict `Ruff` linting and formatting
- Static type testing with `ty`, yes we love [astral](https://astral.sh/)
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

    ```bash
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

### Roadmap

- solve dynamic versioning with tags
- add license classifiers in `pyproject.tom`l
- Replace `hatch` with `uv` (one day)
- use `ty` as type checker, yes we love [astral.sh](https://astral.sh/) stuff..!
- us devcontainer
- docs template with mkdocs
- github actions
- issue template
- docker setup
- app vs package
- pytest, coverage, etc
- typedsettings and cyclopts with examples
- dependabot
- pypi
- [Changelog](https://keepachangelog.com/en/1.1.0/)
- Add proper testing with [this](https://github.com/KyleKing/copier-template-tester/tree/main/docs)
- Add profiles like [this](https://github.com/NLeSC/python-**template**)
- Add proper messages
- Replace `uv-dynamic-version` with the features from [commitizen](https://github.com/commitizen-tools/commitizen) (and also changelog)
- Add contributors: <https://github.com/all-contributors/all-contributors>
- Make print embbeder a separate action/package, and ask to include it

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
