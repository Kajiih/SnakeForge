"""Metadata about the package."""
from ._version import version

__module_name__ = "{{ module_name }}"  # Not dynamic
# __version__ = "{{ project_version }}"
__version__ = version
__authors__ = ["{{ author_fullname }}"]
__author_emails__ = ["{{ author_email }}"]

# === URLs ===
# https://packaging.python.org/en/latest/specifications/well-known-project-urls/#well-known-labels
__repo_url__ = "{{ repo_url }}"
__issues_url__ = f"{__repo_url__}/issues"
__changelog_url__ = f"{__repo_url__}/blob/main/CHANGELOG.md"
__documentation_url__ = "https://{{ package_name }}.readthedocs.io"
