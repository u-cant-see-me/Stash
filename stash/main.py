import typer
from rich import print
from stash.commands.upload import upload_logic
from stash.commands.download import download_logic
from stash.config import config_settings
from typing import List
from stash.utils.banner import banner

app = typer.Typer(invoke_without_command=True,help="upload and download files temporarily from your command line")

def upload(     
        files: List[str] = typer.Argument(...),
        informative:bool=typer.Option(False,"-i","-informative",help="ask before uploading"),
        copy_to_clipboard :bool =typer.Option(False,"-c","-copy",help="copy to clipboard")
    ):
    upload_logic(files,informative,copy_to_clipboard)


def config(
        url:str=typer.Option(None,"--url",help="accepts backend url"),
        store:str= typer.Option(None,"--store",help="accepts storage location"),
        show:bool= typer.Option(None,"--show",help="shows current configuration"),
        ):
     config_settings(url,store,show)

def download(key:str):
    download_logic(key)

"""upload aliases"""
app.command(name="upload",help="uploads file to backend temporarily ,\nuse -c to automatically copy to clipboard ,\nuse -i for asking before uploading each file \n::stash upload <file_name> -c")(upload)
app.command(name="u",help="alias of upload :: stash u <file_name>")(upload)


"""download aliases"""
app.command(name="download",help="download files from backend,use -i for asking before downloading each file")(download)
app.command(name="key",help="alias of download :: stash key <stash-key>")(download)
app.command(name="k",help="aliad of download :: stash k <stash-key>")(download)

app.command(name="config",
            help="update config \nupdating url :: stash config --url <backend_url> \nupdating storage location :: stash config --store <directory_name>\nsee configuration :: stash config --show \n"
            )(config)
    
@app.callback(invoke_without_command=True)
def main(ctx :typer.Context):
    if ctx.invoked_subcommand:
        return 
    banner()


if __name__ == "__main__":
    app()
