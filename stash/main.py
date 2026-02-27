import typer
from rich import print
from stash.commands.upload import upload_logic
from stash.commands.download import download_logic
from stash.config import config_settings
from typing import List
from stash.utils.banner import banner

app = typer.Typer(invoke_without_command=True)

def upload(     
        files: List[str] = typer.Argument(...),
        informative:bool=typer.Option(False,"-i","-informative"),
        copy_to_clipboard :bool =typer.Option(False,"-c","-copy")
    ):
    upload_logic(files,informative,copy_to_clipboard)


def config(
        url:str=typer.Option(None,"--url"),
        store:str= typer.Option(None,"--store")
        ):
     config_settings(url,store)

def download(key:str):
    download_logic(key)

"""upload aliases"""
app.command(name="upload")(upload)
app.command(name="u")(upload)

app.command(name="config")(config)

"""download aliases"""
app.command(name="key")(download)
app.command(name="k")(download)


    
@app.callback(invoke_without_command=True)
def main(ctx :typer.Context):
    if ctx.invoked_subcommand:
        return 
    banner()


if __name__ == "__main__":
    app()
