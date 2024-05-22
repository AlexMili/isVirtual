**isVirtual** is a very simple tool to detect if the current script is within a virtual environment.

# Disclaimer

The goal of this project was to play around with the process to publish to [Pypi](https://pypi.org). The code of this module is coming from this [stackoverflow thread](https://stackoverflow.com/questions/1871549/how-to-determine-if-python-is-running-inside-a-virtualenv).

If you find use cases in which it doesn't work please open an [issue](https://github.com/AlexMili/isVirtual/issues). I intend to maintain this small package even if it can be seen as *"useless"*.

# Install

```bash
pip install isvirtual
```

# Usage

Within a python script:
```python
from isvirtual import is_virtual_env

if __name__ == "__main__":
    if is_virtual_env() is True:
        print("You are within a virtual environment")
    else:
        print("You are not in a virtual env")
```

CLI mode:
```console
$ isvirtual
Yes
```

# License

This project is licensed under the terms of the MIT license.
