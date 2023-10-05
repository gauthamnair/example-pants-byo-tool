import itertools

from pants.backend.byolinter.lib import ByoTool, SystemBinaryExecutable, PythonToolExecutable, collect_byo_rules
from pants.backend.python.target_types import ConsoleScript

confs = [
    ByoTool(
        goal="lint",
        options_scope='byo_markdownlint',
        name="MarkdownLint",
        help="A markdown linter based on your installed markdown lint.",
        executable=SystemBinaryExecutable("markdownlint", tools=["node"]),
        file_glob_include=["**/*.md"],
        file_glob_exclude=["README.md"],
    ),
    ByoTool(
        goal="lint",
        options_scope='byo_flake8',
        name="byo_Flake8",
        help="Flake8 linter using the flake8 you have specified in a resolve",
        executable=PythonToolExecutable(
            main=ConsoleScript("flake8"),
            requirements=["flake8>=5.0.4,<7"],
            resolve="byo_flake8",
        ),
        file_glob_include=["**/*.py"],
        file_glob_exclude=["pants-plugins/**"],
    ),
    ByoTool(
        goal="fmt",
        options_scope='byo_black',
        name="byo_Black",
        help="Black formatter using the black you have specified in a resolve",
        executable=PythonToolExecutable(
            main=ConsoleScript("black"),
            requirements=[
                "black>=22.6.0,<24",
                'typing-extensions>=3.10.0.0; python_version < "3.10"',
            ],
            resolve="byo_black",
        ),
        file_glob_include=["**/*.py"],
        file_glob_exclude=["pants-plugins/**"],
    )
]


def target_types():
    return []


def rules():
    return collect_byo_rules(confs)
