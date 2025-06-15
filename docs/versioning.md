# Versioning

The best way to increment versions is to rely on **Commitizen**. Run `cz bump` ([docs here](https://commitizen-tools.github.io/commitizen/commands/bump/)) to change version.
You can also modify the version manually in the `__about__.py` file of the main module or do it with `hatch` by running `hatch version major|minor|patch`. But in that case, you should also **create a tag** on the repo, or the version will be missing.

The version starts at `0.0.0` and will be incremented to `0.1.0` by commitizen at your first `cz bump` after adding your first feature.

When it will be supported, pushing a version tag will automatically run a github action to publish the new version on **PyPI**.
