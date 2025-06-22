# Documentation

The documentation is created with [mkdocs](https://www.mkdocs.org/) and with the theme [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

By default we use the plugin [mkdocstrings](https://mkdocstrings.github.io/) to create the documentation from the docstrings inside the source code.

## TODO

### General

- Add example of usage of main included extensions
- Setup a [glossary with `abbr` + `pymdownx.snippets` extensions](https://squidfunk.github.io/mkdocs-material/reference/tooltips/?h=tooltips#adding-a-glossary)
- Check [other python-markdown-extensions](https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/)

### Mkdocstrings

- Add [inventories](https://mkdocstrings.github.io/python/usage/#inventories) to referenced dependencies
- Add `griffe-fieldz` extension when we found [why the extension module is not found](https://github.com/pyapp-kit/griffe-fieldz/issues/24)
- Add `griffe_inherited_method_crossrefs` extension when we found [why the the griffe.exceptions module is not found](https://github.com/MatthewLeoLaporte/griffe-inherited-method-crossrefs/issues/18)
