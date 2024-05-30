import typer
from typing_extensions import Annotated

from isvirtual import check_dir, is_virtual_env


app = typer.Typer(add_completion=False)


@app.command(help="Check if you are currently in a virtual env")
def check() -> None:
    if is_virtual_env() is True:
        print("Yes")
    else:
        print("No")


@app.command(help="Scan if the given directory is linked to a virtual env")
def linked(
    path: Annotated[
        str,
        typer.Argument(),
    ] = ".",
) -> None:
    print(path)
    if check_dir(path) is True:
        print("Yes")
    else:
        print("Virtual environment not found")
