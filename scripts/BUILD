file(
    name="stuff-script",
    source="stuff.sh",
    tags=["scripts"]
)

run_shell_command(
    name="lint-stuff-script",
    command="shellcheck stuff.sh",
    execution_dependencies=[":stuff-script"]
)
