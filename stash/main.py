import typer
from rich import print
from rich.console import Console
from rich.text import Text
from stash.commands.upload import upload
from stash.commands.download import download
from typing import List

app = typer.Typer(invoke_without_command=True)
console = Console()

@app.callback(invoke_without_command=True)
def main(
    ctx:typer.Context,
    target: List[str] = typer.Argument(None),
    download_mode:bool=typer.Option(False,"-key","-k"),
    informative:bool=typer.Option(False,"-i","-informative"),
    copy_to_clipboard :bool =typer.Option(False,"-c","-copy")
):
    if ctx.invoked_subcommand is None:
        if not target:
            text = Text("STASH", style="bold cyan")
            text.stylize("bold magenta", 0, 2)
            print(text)
            print("Upload files on temporary storage and download them through key")
            print("\nUse --help to see available commands.\n")
            print(":: [white]stash <file_name/source>[/white] \n")
            print("Use -k or -key to download files \n:: stash [green]-k <stash-key>\n")
        elif not download_mode:
            upload(target,informative,copy_to_clipboard)
        else:
            download(target[0])

if __name__ == "__main__":
    app()
