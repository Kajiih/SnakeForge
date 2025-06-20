# GitHub Actions

We use pinned actions automatically updated by `dependabot` for security (check [zizmor's audit rules](https://docs.zizmor.sh/audits/) to learn more about the security issue with GitHub actions).

You can use [act](https://github.com/nektos/act) to test your GitHub actions locally.

## Default Workflows

### CI

- Lint and check format with `ruff`
- Static type check with `basedpyright`

### Publishing/Release

After you create a new tag with `cz bump` and push them: `git push && git push --tags`, the release workflow will be triggered.

You will need to create a PyPI account and create a [trusted publisher](https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/) for your repository with the `package_name`, `repository_namespace`,`repository_name` as set in the answers. Select `publish.yaml` as workflow name and `pypi` as environment name.

The workflow will:

- Creates a new release on GitHub
- Publish the new version to PyPI

## TODOs

- ✅ Check that `uv` cache works
- ✅ Check that `md test reports` are generated
- Fix test workflow to upload coverage only once (combine?)
- Create `release` workflow
- Check if more actions should be added
- Improve changelog/release notes
- Add guide to create trusted publisher after generating the project
