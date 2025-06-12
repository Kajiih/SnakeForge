# Licenses

## Adding licenses

Added licenses should be taken from the [SPDX License List](https://spdx.org/licenses/).

1. Add license text ([e.g.](https://spdx.org/licenses/0BSD.html)) in the [licenses folder](/includes/licenses/) under the name `<license_short_identifier>.jinja`. Do NOT add the header, this is for the code files and we currently do not automatic license headers input.

2. Add the license choice in the `copyright_license` key in the [project's related questions](/copier/questions/project.yaml)
   1. The choice name should be `<license_full_name> (<license_short_identifier>)`
   2. The value should be `<license_short_identifier>`

### Example

You want to add BSD Zero Clause License.

1. Add the [license's text](https://spdx.org/licenses/0BSD.html) obtained on [SPDX Licence List](https://spdx.org/licenses/) in [0BSD.jinja](/includes/licenses/0BSD.jinja)
2. Replace the `replaceable` text in red with the appropriate variable or constant value: `Copyright (C) YEAR by AUTHOR EMAIL` becomes `Copyright (C) {{ copyright_year }} by {{ copyright_holder }} {{ author_email }}`. You don't always have to replace all red text, like for [MIT](https://spdx.org/licenses/MIT.html).
3. Add the `copyright_license` choice in [copier/questions/project.yaml](/copier/questions/project.yaml)

    ```yaml
    ...
    copyright_license:
        ...
        choices:
            ...
            BSD Zero Clause License (0BSD):
                value: 0BSD
            ...
    ...
    ```

4. Create a pull request

TODO: Also add tests?
TODO: Add headers and hooks to add headers to files.
TODO: Use an API to get licenses: e.g. [GitHub license API](https://docs.github.com/en/rest/licenses/licenses?apiVersion=2022-11-28)
