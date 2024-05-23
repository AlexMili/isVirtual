**isVirtual** is a very simple tool to detect if the current script is within a virtual environment.

# Disclaimer

The goal of this project was to play around with the process to publish to [Pypi](https://pypi.org). The code of this module is coming from this [stackoverflow thread](https://stackoverflow.com/questions/1871549/how-to-determine-if-python-is-running-inside-a-virtualenv).

If you find use cases in which it doesn't work please open an [issue](https://github.com/AlexMili/isVirtual/issues). I intend to maintain this small package even if it can be seen as *"useless"*.

# Install

```bash
pip install isvirtual
```

# Usage

This lib can be used within a python script or as a command line.

## Python
Simple check:
```python
from isvirtual import is_virtual_env

if __name__ == "__main__":
    if is_virtual_env() is True:
        print("You are within a virtual environment")
    else:
        print("You are not in a virtual env")
```

You can also check if you are specifically in a `venv` or `virtualenv` environment:
```python
from isvirtual import is_venv, is_virtualenv

if __name__ == "__main__":
    if is_venv() is True:
        print("You are in a venv")
    elif is_virtualenv() is True:
        print("You are in a virtualenv")
    else:
        print("You are not in a virtual env")
```

You can also get the info from the env coming from `pyvenv.cfg`. The `sys.prefix` data is added to the original config file:
```python
from isvirtual import is_virtual_env, pyvenv_cfg

if __name__ == "__main__":
    if is_virtual_env() is True:
        data = pyvenv_cfg()
        print(data["home"])
```


## CLI
```console
$ isvirtual
Yes
```

# License

This project is licensed under the terms of the MIT license.
