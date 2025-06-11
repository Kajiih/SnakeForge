import compileall
import shutil
import tempfile
from pathlib import Path

from copier import run_copy


def test_template_compiles():
    output_dir = Path(tempfile.mkdtemp())
    try:
        _ = run_copy(
            src_path=".",
            dst_path=output_dir,
            data={
                "project_name": "MyAwesomeProject",
                "project_description": "An amazing project",
                #     "project_keywords": "python,myawesomeproject",
                #     "development_status": "Beta",
                #     "copyright_license": "MIT License",
                #     "copyright_year": "2025",
                #     "author_fullname": "Julian Paquerot",
                #     "author_username": "julianpaquerot",
                #     "author_email": "julian.paquerot@example.com",
                #     "organization_name": "OpenAI",
                #     "copyright_holder": "OpenAI",
                #     "repo_platform": "github",
                #     "repo_namespace": "openai",
                #     "repo_name": "my-awesome-project",
                #     "package_name": "my-awesome-project",
                #     "module_name": "my_awesome_project",
                #     "cli_name": "my-awesome-project",
                #     "coverage_threshold": 85,
                #     "platforms": ["macos", "linux", "windows"],
                #     "min_py": "3.12",
                #     "max_py": "3.14",
                #     "default_py": "3.14",
            },
            defaults=True,
            unsafe=True,
            vcs_ref="HEAD",  # Optional, but safer for testing
            quiet=True,
            # answers_file="answers.yml",
        )
        # Run your checks, e.g., test if a file was created
        assert (output_dir / "pyproject.toml").exists()

        # Check if Python files compile

        assert compileall.compile_dir(str(output_dir), quiet=True)

    finally:
        shutil.rmtree(output_dir)
