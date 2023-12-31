# adhoc command experiments

Tests exploring possibilities around https://github.com/pantsbuild/pants/issues/17729


## To run

You need the pants branch referenced in https://github.com/pantsbuild/pants/pull/19954 . Then set:
```shell
$ export PANTS_SOURCE=<your-local-pants-with-branch-installed>
```

You need markdownlint installed and available on your path (as well as its dependency `node`)

Then you can run:
```shell
$ pants fmt ::
...

+ black_tool made changes.
$ git diff hello.py
-    print('Hello world')  # black is not going to like these single quotes
+    print("Hello world")  # black is not going to like these single quotes

$ pants_from_sources lint ::

✓ black_tool succeeded.
✓ flake8 succeeded.
✓ markdownlint succeeded.
```

## Things that work

You can subset by folder:
```shell
$ pants lint docs/subsection/

✓ markdownlint succeeded.
```

or by target address:
```shell
$ pants lint //hello.py

✓ black_tool succeeded.
✓ flake8 succeeded.
```

You can use the regular mechanisms to skip or select linters
```shell
$ pants lint --only=flake8 ::

✓ flake8 succeeded.
$ pants lint --flake8-skip ::

✓ black_tool succeeded.
✓ markdownlint succeeded.
```

And there is some minimal help:
```shell
$ pants help flake8
`flake8` subsystem options
--------------------------

Lint with Flake8. Tool defined in //:flake8_linter
 
Activated by pants.backend.experimental.code_quality_tool
Config section: [flake8]
 
  --[no-]flake8-skip
  PANTS_FLAKE8_SKIP
  skip
      default: False
      current value: False
      If true, don't use Flake8 when running `pants lint`.
```
