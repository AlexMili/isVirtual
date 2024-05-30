**isVirtual** is a tool to detect if the current directory is linked to a virtual environment, get the config of this env and more. Work with venv, virtualenv, pipenv, poetry and soon hatch and pdm.

# Install

```bash
pip install isvirtual
```

# Usage

This lib can be used within a python script or as a command line.

## Python
Simple check:
```python
from isvirtual import is_virtual

if __name__ == "__main__":
    if is_virtual() is True:
        print("You are within a virtual environment which can either be venv, virtualenv or conda.")
    else:
        print("You are not in a virtual env")
```

You can also check if you are specifically in a `venv`, `virtualenv` or `conda` environment:
```python
from isvirtual import is_venv, is_virtualenv, is_conda

if __name__ == "__main__":
    if is_venv() is True:
        print("You are in a venv")
    elif is_virtualenv() is True:
        print("You are in a virtualenv")
    elif is_conda() is True:
        print("You are in a conda env")
    else:
        print("You are not in a any type of virtual env")
```

You can also get the info from the env coming from `pyvenv.cfg` or load equivalent data from `conda` config. The `sys.prefix` data is added to the original config file under the key `prefix`:
```python
from isvirtual import get_config

if __name__ == "__main__":
    data = get_config()
    print(data["home"])
```
Result:
```console
home = /path/to/venv/python/bin
include-system-site-packages = false
version = 3.10.14
prefix = /path/to/venv/dir
prompt = nameOfYourProject
```

Note that virtual environment created with `virtualenv` have more keys and the key `prompt` is not present by default in `venv` created environments.

You can also check if the terminal from which the script has been launched is in a virtual env:
```python
if running_from_activated_env() is True:
    print("The script is running from a terminal with an activated virtual env")
```

Note that this function check the existence of `VIRTUAL_ENV`. It is set by the activate script, but a virtual env can be used without activation by directly running an executable from the virtual env's bin/ (or Scripts on Windows) directory, in which case `VIRTUAL_ENV` will not be set. Or a non-virtual env Python binary can be executed directly while a virtual env is activated in the shell, in which case `VIRTUAL_ENV` may be set in a Python process that is not actually running in that virtual env.

[Source](https://stackoverflow.com/a/1883251)

You can find if a given directory is attached to a virtual env:
```python
from isvirtual import check_dir

if __name__ == "__main__":
    if check_dir("/some/dir/path") is True:
        print("Virtual environment found")
    else:
        print("404 Not Found")
```

You can recursively scan a directory to get all virtual environments in it:
```python
from isvirtual import scan_dir

if __name__ == "__main__":
    scanned = scan_dir("/some/dir/path")
    if len(scanned) > 0:
        print(f"Found {len(scanned)} virtual env(s)")
    else:
        print("No virtual env found")
```

## CLI
```console
$ isvirtual --help
Usage: isvirtual [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
│ check   Check if you are currently in a virtual env                                    │
│ info    If the given directory is linked to a virtual env, show its info               │
│ scan    Scan the given directory recursively to find all virtual environment in it     │
╰────────────────────────────────────────────────────────────────────────────────────────╯
```

Check if a virtual env is currently activated (support conda):
```console
$ isvirtual check
Yes
```

Show info of current directory's virtual env info:
```console
$ isviritual info .
home=/usr/local/opt/python@3.10/bin
include-system-site-packages=false
version=3.10.14
path=/Users/MyUserName/MyDir/.venv
source=venv
```
Also display with the `source` key if the virtual env has been created through `venv`, `virtualenv`, `poetry` and `pipenv`.

# License

This project is licensed under the terms of the MIT license.
