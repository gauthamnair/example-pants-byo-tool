import itertools

from pants.backend.byolinter.lib import ByoLinter


confs = [
    ByoLinter(
        options_scope='byo_shellcheck',
        name="Shellcheck",
        help="A shell linter based on your installed shellcheck",
        command="shellcheck",
        file_extensions=[".sh"],
    ),
    ByoLinter(
        options_scope='byo_markdownlint',
        name="MarkdownLint",
        help="A markdown linter based on your installed markdown lint.",
        command="markdownlint",
        file_extensions=[".md"],
    )
]


def target_types():
    return []


def rules():
    return list(itertools.chain.from_iterable(conf.rules() for conf in confs))