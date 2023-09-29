# adhoc command experiments

Tests exploring possibilities around https://github.com/pantsbuild/pants/issues/17729


## To run

You need the pants branch referenced in https://github.com/pantsbuild/pants/pull/19954

Then you can run:
```shell
$ export PANTS_SOURCE=<your-local-pants-with-branch-installed>
$ pants lint ::
Pantsd has been turned off via Env.
12:04:01.20 [INFO] Completed: Run Shellcheck
12:04:01.20 [INFO] Completed: pants.backend.byolinter.lib.build.run_ByoLint_byo_shellcheck - byo_shellcheck succeeded.
12:04:01.31 [INFO] Completed: Run MarkdownLint
12:04:01.31 [INFO] Completed: pants.backend.byolinter.lib.build.run_ByoLint_byo_markdownlint - byo_markdownlint succeeded.
12:04:02.91 [INFO] Completed: Lint with Flake8 - flake8 succeeded.
Partition: ['CPython==3.9.*']



✓ byo_markdownlint succeeded.
✓ byo_shellcheck succeeded.
✓ flake8 succeeded.
```
as long as you have shellcheck and markdownlint (and whichever dependencies they have) installed on your path.
