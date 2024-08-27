import threading as th
from flask import *

class Webinterface:
    def __init__(self, serverName):
        self.serverName = serverName
        self.webinterface = Flask(__name__)
        self.webinterface.config["SERVER_NAME"] = self.serverName
        self.addEndpoints()

    def addEndpoints(self):
        self.webinterface.add_url_rule("/", "upload_startPage", self.uploadStartpage, methods=["GET"])
        self.webinterface.add_url_rule("/upload_no_file_selected", "upload_noFileSelected", self.uploadNoFileSelected, methods=["GET"])
        self.webinterface.add_url_rule("/upload_invalid_file_format", "upload_invalidFileFormatSelected", self.uploadInvalidFileFormat, methods=["GET"])
        self.webinterface.add_url_rule("/upload", "upload", self.upload, methods=["GET", "POST"])
        self.webinterface.add_url_rule("/transcription_process", "transcriptionProcess", self.startTranscriptionProcess, methods=["GET"] )
        self.webinterface.add_url_rule("/correct_transcript", "correctionPage", self.correctionPage, methods=["GET"])
        self.webinterface.add_url_rule("/download", "download", self.downloadPage, methods=["GET"])

    def run(self, **kwargs):
        self.webinterface.run(**kwargs)

    def uploadStartpage(self):
        return render_template("") 

    def uploadNoFileSelected(self):
        return render_template("")

    def uploadInvalidFileFormat(self):
        return render_template("")
    
    def upload(self):
        return redirect(url_for("transcriptionProcess"))
    
    def startTranscriptionProcess(self):
        th.Thread(target=self.transcriptionProcess, daemon=True).start()
        return render_template("")
    
    def transcriptionProcess(self):
        pass

    def correctionPage(self):
        return render_template("")
    
    def downloadPage(self):
        return render_template("")
