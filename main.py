import os.path as osp
import sys

version_path = osp.join(osp.dirname(__file__), "VERSION.md")

if osp.exists(version_path):
    with open(version_path, "r") as f:
        __version__ = f.readline()


def is_virtual_env():
    # The check for sys.real_prefix covers virtualenv, the equality of
    # non-empty sys.base_prefix with sys.prefix covers venv.
    # note: Python versions before 3.3 don't have sys.base_prefix
    # if you're not in virtual environment
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def is_virtual_env_cli():
    if is_virtual_env() is True:
        print("Yes")
    else:
        print("No")
