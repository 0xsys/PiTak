import dropbox

class exfiltration:
    def __init__(self) -> None:
        pass
    
    def connect(self):
        try:
            self.connection = dropbox.Dropbox() # Access token needed, omitted for security reasons
        except Exception:
            exit("There was an error connecting to the Dropbox API!")

    def selfPrint(self):
        print(self.connection)

a = exfiltration
a.connect("xx")
a.selfPrint("xx")

