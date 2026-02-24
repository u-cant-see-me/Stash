import typer
from rich import print
from stash.commands.upload import upload
from stash.commands.download import download
from typing import List

app = typer.Typer(invoke_without_command=True)

@app.callback(invoke_without_command=True)
def main(
    target: List[str] = typer.Argument(...),
    download_mode:bool=typer.Option(False,"-key","-k"),
    informative:bool=typer.Option(False,"-i","-informative"),
    copy_to_clipboard :bool =typer.Option(False,"-c","-copy")
):
    print(download_mode)
    if not download_mode:
        upload(target,informative,copy_to_clipboard)
    else:
        download(target[0])

if __name__ == "__main__":
    app()
