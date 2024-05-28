import configparser
import glob
import json
import os
import sys

config = None


def is_virtual() -> bool:
    return is_virtual_env() or is_conda()


def is_virtual_env() -> bool:
    # The check for sys.real_prefix covers virtualenv, the equality of
    # non-empty sys.base_prefix with sys.prefix covers venv.
    # note: Python versions before 3.3 don't have sys.base_prefix
    # if you're not in virtual environment
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def get_config() -> dict:
    dconf = {}
    if is_virtual_env() is False:
        dconf = _conda_cfg()
    else:
        prefix = _get_prefix()
        _read_config(os.path.join(prefix, "pyvenv.cfg"))

        dconf = dict(config["root"])
        dconf["prefix"] = prefix

    return dconf


def _conda_cfg() -> dict:
    data = {}

    data["home"] = os.path.join(os.environ["CONDA_PREFIX"], "bin")
    data["prefix"] = _get_prefix()
    data["include-system-site-packages"] = False
    data["prompt"] = os.environ["CONDA_DEFAULT_ENV"]

    path = os.path.join(os.environ["CONDA_PREFIX"], "conda-meta", "python*")

    files = glob.glob(path)
    if len(files) > 0:
        with open(files[0], "r") as fp:
            conda_info = json.load(fp)

    data["version"] = conda_info["version"]

    return data


def is_venv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(os.path.join(prefix, "pyvenv.cfg"))

    if is_virtualenv() is False:
        return True
    else:
        return False


def is_virtualenv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(os.path.join(prefix, "pyvenv.cfg"))

    if "virtualenv" in config["root"]:
        return True
    else:
        return False


def is_conda() -> bool:
    is_conda = False
    try:
        os.environ["CONDA_DEFAULT_ENV"]
        is_conda = True
    except Exception:
        pass
    try:
        os.environ["CONDA_PREFIX"]
        is_conda = True
    except Exception:
        pass

    return is_conda


def _get_prefix() -> str:
    return sys.real_prefix if hasattr(sys, "real_prefix") else sys.prefix


def _read_config(path: str) -> None:
    global config
    if config is None:
        conf = configparser.ConfigParser()
        with open(path) as stream:
            # Add fake section name to make pyvenv.cfg compatible with ConfigParser
            conf.read_string("[root]\n" + stream.read())
        config = conf


def is_virtual_cli() -> None:
    if is_virtual():
        print("Yes")
    else:
        print("No")
