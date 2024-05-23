import configparser
import os.path as osp
import sys

config = None


def is_virtual_env() -> str:
    # The check for sys.real_prefix covers virtualenv, the equality of
    # non-empty sys.base_prefix with sys.prefix covers venv.
    # note: Python versions before 3.3 don't have sys.base_prefix
    # if you're not in virtual environment
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def pyvenv_cfg() -> dict:
    if is_virtual_env() is False:
        return {}

    prefix = _get_prefix()
    _read_config(osp.join(prefix, "pyvenv.cfg"))

    dconf = dict(config["root"])
    dconf["prefix"] = prefix

    return dconf


def is_venv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(osp.join(prefix, "pyvenv.cfg"))

    if "virtualenv" in config["root"]:
        return False
    else:
        return True


def is_virtualenv() -> bool:
    if is_virtual_env() is False:
        return False

    prefix = _get_prefix()
    _read_config(osp.join(prefix, "pyvenv.cfg"))

    if "virtualenv" in config["root"]:
        return True
    else:
        return False


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


def is_virtual_env_cli() -> None:
    if is_virtual_env() is True:
        print("Yes")
    else:
        print("No")
