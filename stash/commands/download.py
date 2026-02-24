import requests
import json
from rich import print
from rich.console import Console

def download(stashkey:str):
    BACKEND_URL = "https://stashit-uqpt.onrender.com"
    serverUrl = f"{url}/api/file/download"
    params = { "stashKey":stashkey } 
    print("fetching download urls")
    console = Console()
    with console.status(" Processing..",spinner="shark") as status:
        try:
            response = requests.get(serverUrl,params= params)
            data = json.loads(response.text)
        except Exception as e:
            print("failed to load data from database exception",e )

    if response.status_code == 200 :
        downloadUrls = data["downloadUrls"]
        print("Downloading ...... ")

        for url in downloadUrls:
            name = url["name"]
            downloadLink = url["downloadUrl"]
            with console.status(" Processing...",spinner="dots") as status:
                try:
                    downloadRes = requests.get(downloadLink)
                except:
                    print("/n [red] failed to process request /n request ended with exception [/red]",e)
            if downloadRes.status_code == 200 :
                print("-> file :",name)
                with console.status(" Downloading..",spinner="shark") as status:
                    try:
                        with open(name , "wb" ) as f:
                            f.write(downloadRes.content)
                        print("downloaded successfully")
                    except Exception as e:
                        print(f"[red] failed to download file {name} with exception {e}[/red]")
            else:
                print("failed downloading")
    else:
        print(f"server responded with status code {response.status_code} \n response :[red]{json.loads(response.text)["message"]}[/red]")
                
