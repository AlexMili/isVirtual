import typer
from typing_extensions import Annotated

from sty import fg
from isvirtual import check_dir, is_virtual_env


app = typer.Typer(add_completion=False)


@app.command(help="Check if you are currently in a virtual env")
def check() -> None:
    if is_virtual_env() is True:
        print("You are in a virtual environment")
    else:
        print("You are NOT in a virtual environment")


@app.command(help="If the given directory is linked to a virtual env, show its info")
def info(
    path: Annotated[
        str,
        typer.Argument(),
    ] = ".",
) -> None:
    config = check_dir(path)
    if len(config) > 0:
        for k, v in config.items():
            print(f"{fg.blue}{k}={fg.green}{v}")
    else:
        print(f"{fg.red}Virtual environment not found")
