import requests
from rich import print
from rich.console import Console
from pathlib import Path
import mimetypes
import json
from typing import List
from nanoid import generate 
import pyperclip
import math
from rich.table import Table

console = Console()

def createMetadataList(files):
    metadataList = []

    for f in files:
        file = Path(f)
        if not file.is_file():
            print(f"[red] invalid file type {file}")
            continue
        size = file.stat().st_size 
        formattedSize = getSize(size)
        data = {
            "fileInfo":{
                "id": generate(size=10),
                "name": file.name,
                "type": mimetypes.guess_type(file),
                "size": size,
                "formattedSize": {
                        "size": formattedSize,
                        "valid": size < 50*1024*1024 
                    }
                },
            "filePath":file,
            "status":"pending"
            }
        metadataList.append(data)
    return metadataList

def getSize(x):
    n = x
    bytes = ['Kb','Mb','Gb','Tb']
    count = 0
    while n > 10:
        n = n / 1024 
        count += 1
    return f"{math.floor(x / (math.pow(1024,count))*100)/100}{bytes[count-1]}"


def displayFiles(files):
    print("name        size         valid")
    for file in files:
        f= Path(file)
        size = f.stat().st_size
        print(f.name ,size,getSize(size))


def upload(files:List[str],informative:bool,copyToClipboard:bool):
    if not Path(files[0]).is_file():
        print("invalid input ")
        return 
    BACKEND_URL = "https://stashit-uqpt.onrender.com"
    serverUrl = f"{BACKEND_URL}/api/file/upload"
    print(files)
    metadataList = createMetadataList(files)

    filteredMetadata = [f["fileInfo"] for f in metadataList ]

    payload = {
            "files": filteredMetadata,
            "expiry": "once"
            }
    print("\n[green]-> registering files on database \n")
    with console.status("Processing..",spinner="dots") as status:
        response = requests.post(serverUrl,json = payload)
        res = json.loads(response.text)
    signedUrls = res["signedUrls"]
    stashKey = res["stashKey"]
    try:
        for url in signedUrls:
            found = False
            for metadata in metadataList:
                if metadata["fileInfo"]["id"]== url["id"]:
                    data = metadata
                    found = True
            if found :
                # if informative :
                #     inform = input(f"upload file y/yes ")
                #     if not (inform == 'y' or inform.lower() == "yes" or inform == " "):
                #         continue
                with console.status(f" Processing.. {url["name"]} size : {data["fileInfo"]["formattedSize"]["size"]}",spinner="dots") as status:
                    with open(data["filePath"], "rb" ) as f:
                        if f:
                            response = requests.put(url["uploadUrl"]
                                                ,data = f,
                                                headers= {"Content-Type" :
                                                    "application/octet-stream"
                                                    }
                                            )
                        
                print(f"[green]-> {url["name"]} sucessfully uploaded")

    except FileNotFoundError:
        print("error file not found")
    except Exception as e:
        print(f"some exception : {e}")

    if copyToClipboard:
        try:
            pyperclip.copy(stashKey)
            print("\n-> copied stash key to clipboard")
        except:
            print("[red]failed copying to clipboard")



    print("\n----------------------------------------------------------------------\n")
    print(f"\t[bold blue] {stashKey}")
    print("\n----------------------------------------------------------------------\n")
    
    # table = Table(title="Upload Summary")
    # table.add_column("File", style="cyan")
    # table.add_column("Size", style="magenta")
    # table.add_column("Status", style="green")
    # table.add_row("file.txt", "2.3 MB", "Uploaded")
    # console.print(table)

