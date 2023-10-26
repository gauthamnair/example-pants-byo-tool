python_sources()

python_requirement(
    name="black",
    requirements=["black==22.6.0"],
    resolve="byo_black"
)

python_requirement(
    name="typing_extensions",
    requirements=['typing-extensions>=3.10.0.0; python_version < "3.10"'],
    resolve="byo_black"
)


file(
    name="flake8_conf",
    source=".flake8"
)


python_requirement(
    name="flake8",
    requirements=["flake8==5.0.4"],
    resolve="byo_flake8"
)

byolinter(
    name="flake8_linter",
    runnable=":flake8",
    runnable_dependencies=[],
    execution_dependencies=[":flake8_conf"],
    args=["--max-line-length", "100"],
    file_glob_include=["**/*.py"],
    file_glob_exclude=["pants-plugins/**"],
)

system_binary(
    name="node",
    binary_name="node",
    fingerprint=r"v20\.7\.0",
    fingerprint_args=["--version"],
)

system_binary(
    name="markdownlint",
    binary_name="markdownlint",
    fingerprint=r'0\.37\.0',
    fingerprint_args=['--version'],
    fingerprint_dependencies=[':node']
)

byolinter(
    name="markdownlint_linter",
    runnable=':markdownlint',
    runnable_dependencies=[":node"],
    file_glob_include=["**/*.md"],
    file_glob_exclude=["README.md"],
)
