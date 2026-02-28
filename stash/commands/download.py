import os
import requests
import json
from rich import print
from rich.console import Console
from stash.config import loadConfig

def download_logic(stashkey:str):
    config = loadConfig()
    BACKEND_URL = config["BACKEND_URL"]
    DOWNLOAD_DIR = config["DOWNLOAD_DIR"]
    serverUrl = f"{BACKEND_URL}/api/file/download"
    params = { "stashKey":stashkey } 
    print("fetching download urls")
    console = Console()
    with console.status(" Processing..",spinner="dots") as status:
        try:
            response = requests.get(serverUrl,params= params) #fetching download urls from subapase
            data = json.loads(response.text) 
        except Exception as e:
            print("failed to load data from database exception",e )

    if response.status_code == 200 :
        downloadUrls = data["downloadUrls"]
        for url in downloadUrls:
            file_name = url["name"]
            file_path = os.path.join(DOWNLOAD_DIR,file_name)
            downloadLink = url["downloadUrl"]
            with console.status(" Processing...",spinner="dots") as status:
                try:
                    downloadRes = requests.get(downloadLink) #downloading response from each link
                except:
                    print("/n [red] failed to process request /n request ended with exception [/red]",e)
            if downloadRes.status_code == 200 :
                print("[green]:: file :",file_name)
                try:
                    with open(file_path , "wb" ) as f:
                        f.write(downloadRes.content) #writing files from download res into the given location with imported file name
                    print("[green]downloaded successfully")
                except Exception as e:
                    print(f"[red] failed to download file {file_name} with exception {e}[/red]")
            else:
                print("failed downloading")
    else:
        print(f"server responded with status code {response.status_code} \n response :[red]{json.loads(response.text)["message"]}[/red]")
                
