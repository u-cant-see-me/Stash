def printFile(addr):
    try:
        with open(addr,"r") as file:
            content = file.read()
            print("Full content ",content)
            file.seek(0)
            for line in file:
                print("--> " , line.strip())
    except FileNotFoundError:
        print("error file not found")
    except Exception as e:
        print(f"some exception : {e}")
