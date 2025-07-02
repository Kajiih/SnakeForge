<p align="center">
    <em>SnakeForge, the opinionated Python template that gives you what you need, and no more.</em>
</p>

# Your favorite template for Python 🐍

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

You will need accounts on:

- [GitHub](https://github.com/) to host your repository
- [PyPI](https://pypi.org/) to publish your project
- [CodeCov](https://about.codecov.io/sign-up/) to check your project's tests and coverage

Make sure the following dependencies are installed:

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

2. **Generate the Python project**

    We use [Jinja extensions](https://copier.readthedocs.io/en/stable/configuring/#jinja_extensions) and [tasks](https://copier.readthedocs.io/en/stable/configuring/#tasks), so you need to run the command with the [`--trust`](https://copier.readthedocs.io/en/stable/configuring/#unsafe) flag.

    Check [tasks](/copier/tasks.yaml) and [extensions](/extensions.py) to make sure you trust the repository.

    ```shell
    copier copy --trust gh:Kajiih/SnakeForge <path_to_project>
    ```

3. **Finish the project setup**

    Follow the instructions displayed at the end of the generation process to enable all features.

    💡 Your CI/CD workflow will probably fail until you setup everything correctly and remove the code samples to improve code coverage.

4. **Start coding your awesome project!**

    💡 Most of the time, if you want to update something that depends on an answer from the template (e.g., min python version, project description, etc), you better [update the template](#update-your-project) with the new value so that it changes the value everywhere automatically.

### Roadmap

- add license classifiers in `pyproject.tom`
- Replace `hatch` with `uv` (when the build backend is feature complete)
- use `ty` as type checker, yes we love [astral.sh](https://astral.sh/) stuff..!
- use devcontainer
- issue template
- docker setup
- app vs package
- typedsettings and cyclopts with examples
- [Changelog](https://keepachangelog.com/en/1.1.0/)
- Add proper testing with [this](https://github.com/KyleKing/copier-template-tester/tree/main/docs)
- Add profiles like [this](https://github.com/NLeSC/python-**template**)
- Update messages
- code embbedder and print result embedder in precommit hook
- Replace plain tasks by some more practical task runner (invoke, etc)
- Publish github workflow
- Fix codecov test analytics not appearing: [issue](https://github.com/codecov/test-results-action/issues/126)
- Documentation
  - Add [analytics](https://squidfunk.github.io/mkdocs-material/setup/setting-up-site-analytics/)
  - Add [versioning](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/)
  - (maybe) Add [Social cards](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/)

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
