
# Your favorite python project template

## Contents <!-- omit from toc -->

- [📋 Requirements](#-requirements)
- [🚀 Quickstart](#-quickstart)
- [✨ Features](#-features)
  - [Roadmap](#roadmap)
- [Advanced Usage](#advanced-usage)
  - [Update your project](#update-your-project)
- [Resources](#resources)

## 📋 Requirements

Unsure the following dependencies are installed:

- Python>=3.12
- [Copier](https://copier.readthedocs.io/en/stable/)
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

## ✨ Features

- Automatically setups GitHub repository and virtual environment with `uv`
- Configurations for `Ruff`, `Pytest`, `pytest-coverage`
- Dynamic project metadata with `hatch`
- Documentation and Readme template inspired by [FastAPI](https://fastapi.tiangolo.com/) and [Typer](https://typer.tiangolo.com/)

### Roadmap

- Replace `hatch` with `uv`
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
