import os.path as osp

version_path = osp.join(osp.dirname(__file__), "VERSION.md")

if osp.exists(version_path):
    with open(version_path, "r") as f:
        __version__ = f.readline()
