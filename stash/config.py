import os
import json

defaultConfig = {
    "BACKEND_URL":"https://stashit-uqpt.onrender.com",
    "DOWNLOAD_DIR":"."#current directory
}
dir_name = "stash"
file_name = "config.json"
file_path = os.path.join(dir_name,file_name)

def ensureConfig():
    try:
        os.makedirs(dir_name,exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path,"w") as f:
                f.write(json.dumps(defaultConfig))
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: No permission to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    
def loadConfig():
    try:
        ensureConfig()
        with open(file_path , "r") as f:
            data = f.read()
            return json.loads(data)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: No permission to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def updateConfig(config_key,config_value):
    try:
        ensureConfig()
        config = loadConfig()
        with open(file_path,"w") as f:
            config[config_key] = config_value
            f.write(json.dumps(config))

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: No permission to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def config_settings(url:str,store:str,show:bool):
        if url :
            updateConfig("BACKEND_URL",url)
        elif store:
            updateConfig("DOWNLOAD_DIR",store)
        elif show:
            print(loadConfig())
        else:
            print("use url for updating backend url or use store for updating storage location")