import json
import threading as th
from flask import *

import time

class Webinterface:
    def __init__(self, serverName):
        self.serverName = serverName
        self.transcriptionStatus = ""
        self.webinterface = Flask(__name__)
        self.webinterface.config["SERVER_NAME"] = self.serverName
        self.addEndpoints()

    def addEndpoints(self):
        self.webinterface.add_url_rule("/", "upload_startPage", self.uploadStartpage, methods=["GET"])
        self.webinterface.add_url_rule("/upload_no_file_selected", "upload_noFileSelected", self.uploadNoFileSelected, methods=["GET"])
        self.webinterface.add_url_rule("/upload_invalid_file_format", "upload_invalidFileFormatSelected", self.uploadInvalidFileFormat, methods=["GET"])
        self.webinterface.add_url_rule("/upload", "upload", self.upload, methods=["GET", "POST"])
        self.webinterface.add_url_rule("/transcription_process", "transcriptionProcess", self.startTranscriptionProcess, methods=["GET"] )
        self.webinterface.add_url_rule("/transcription_status", "transcription_status", self.getTranscriptionStatus, methods=["GET"])
        self.webinterface.add_url_rule("/correct_transcript", "correctionPage", self.correctionPage, methods=["GET"])
        self.webinterface.add_url_rule("/corrected_transcript", "correctedTranscript", self.getCorrectedTranscript, methods=["GET", "POST"])
        self.webinterface.add_url_rule("/download", "download", self.downloadPage, methods=["GET"])
        self.webinterface.add_url_rule("/download_pdf", "downloadPDF", self.downloadPdf, methods=["GET"])

    def run(self, **kwargs):
        self.webinterface.run(**kwargs)

    def uploadStartpage(self):
        return render_template("upload_startpage.html")

    def uploadNoFileSelected(self):
        return render_template("upload_noFileSelected.html")

    def uploadInvalidFileFormat(self):
        return render_template("upload_invalidFileFormat.html")
    
    def upload(self):
        return redirect(url_for("transcriptionProcess"))
    
    def startTranscriptionProcess(self):
        self.transcriptionStatus = "inProgress"
        th.Thread(target=self.transcriptionProcess, daemon=True).start()
        return render_template("transcriptionProgressPage.html")
    
    def transcriptionProcess(self):
        time.sleep(5) #Placeholder
        self.transcriptionStatus = "done"

    def getTranscriptionStatus(self):
        transcriptionStatus = {"transcriptionStatus":self.transcriptionStatus, 
                               "serverName":self.serverName}
        return json.dumps(transcriptionStatus)

    def correctionPage(self):
        return render_template("correctionPage.html")
    
    def getCorrectedTranscript(self):
        return redirect(url_for("download"))

    def downloadPage(self):
        return render_template("downloadPage.html")
    
    def downloadPdf(self):
        print("Download") #placeholder