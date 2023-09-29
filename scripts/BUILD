file(
    name="stuff-script",
    source="stuff.sh",
    tags=["scripts"]
)

file(
    name="good-script",
    source="good.sh",
    tags=["scripts"]
)

run_shell_command(
    name="lint-stuff-script",
    command="shellcheck stuff.sh",
    execution_dependencies=[":stuff-script"]
)

run_shell_command(
    name="just-ls",
    command="ls",
    execution_dependencies=[":stuff-script"]
)
