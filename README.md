# adhoc command experiments

Tests exploring possibilities around https://github.com/pantsbuild/pants/issues/17729


## To run

You need the pants branch referenced in https://github.com/pantsbuild/pants/pull/19954

You need markdownlint installed and available on your path (as well as its dependency `node`)

Then you can run:
```shell
$ export PANTS_SOURCE=<your-local-pants-with-branch-installed>
$ pants fmt ::
black - byo_black made changes.
  hello.py

+ byo_black made changes.
$ git diff hello.py
-    print('Hello world')  # black is not going to like these single quotes
+    print("Hello world")  # black is not going to like these single quotes

$ pants lint ::

✓ byo_black succeeded.
✓ byo_flake8 succeeded.
✓ byo_markdownlint succeeded.
```
