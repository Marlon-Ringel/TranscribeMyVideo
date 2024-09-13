import json
import threading as th
from flask import *
from flask_bootstrap import Bootstrap5
from dataManager import DataManager
from uploadService import UploadService
from transcriptionService import TranscriptionService

# Class that implements the functionality for the interaction and communication with the client, the management of the 
# application routes and the control flow of function execution. 
class Webinterface:
    
    # Initialization of the Webinterface Object. Initializes Flask and Bootstrap. Registers the endpoints of the application. 
    # Initializes the file system.
    #
    # Class attributes: 
    # serverName: Stores the base_url from the application as a string. 
    # transcriptionStatus: Stores the status of the transcription process as a string.
    def __init__(self):
        self.serverName = ""
        self.transcriptionStatus = ""
        self.webinterface = Flask(__name__)
        self.bootstrap = Bootstrap5(self.webinterface)
        self.addEndpoints()
        DataManager.initailizeFilesystem()

    # Initializes the routes and corresponding handler-functions. 
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

    # Invokes the execution of the Flask services. 
    def run(self, **kwargs):
        self.webinterface.run(**kwargs)

    # Resets the file system. Updates the serverName class attribute with the current base_url. Returns an HTTP
    # response containing the startpage HTML document to the client.
    #
    # Return: 
    # HTTP response containing the startpage HTML document.
    def uploadStartpage(self):
        DataManager.resetFileSystem()
        self.serverName = request.url_root
        return render_template("upload_startpage.html")

    # Returns an HTTP response containing the uploadNoFileSelected error page HTML document to the client.
    #
    # Return: 
    # HTTP response containing the uploadNoFileSelected error page HTML document.
    def uploadNoFileSelected(self):
        return render_template("upload_noFileSelected.html")

    # Returns an HTTP response containing the uploadInvalidFileFormat error page HTML document to the client.
    #
    # Return: 
    # HTTP response containing the uploadInvalidFileFormat error page HTML document.
    def uploadInvalidFileFormat(self):
        return render_template("upload_invalidFileFormat.html")
    
    # Receives an HTTP request. Initializes the UploadService Object and passes it the HTTP request. Uses the 
    # UploadService Object to check if a file was uploaded and has the correct file format. 
    # If no file was uploaded: Redirects the client to the uploadNoFileSelected error page. 
    # If the file has the wrong format: Redirects the client to the uploadInvalidFileFormat error page.
    # If both checks were successful. Redirects the client to the transcriptionProgressPage. 
    #
    # Return: 
    # HTTP redirect to the appropriate page depending on the outcome of the performed checks.
    def upload(self):
        uploadService = UploadService(request)

        if uploadService.fileNotUploaded():
            return redirect(url_for('upload_noFileSelected'))
        
        if not uploadService.validateFileFormat():
            return redirect(url_for('upload_invalidFileFormatSelected')) 
        
        return redirect(url_for("transcriptionProcess"))
    
    # Updates the transcriptionStatus class attribute to "inProgress". Starts the transcription Process in a separate thread. 
    # Returns an HTTP response containing the transcriptionProgressPage HTML document to the client. 
    #
    # Return: 
    # HTTP response containing the transcriptionProgressPage HTML document.
    def startTranscriptionProcess(self):
        self.transcriptionStatus = "inProgress"
        th.Thread(target=self.transcriptionProcess, daemon=True).start()
        return render_template("transcriptionProgressPage.html", videoFileName=DataManager.getVideoFileName())
    
    # Initializes the TranscriptionService Object. Uses the TranscriptionService Object to generate a transcript of the 
    # currently processed video file. Updates the transcriptionStatus class attribute to "done". 
    def transcriptionProcess(self):
        transcriptionService = TranscriptionService()
        transcriptionService.generateTranscription()
        self.transcriptionStatus = "done"

    # Creates a JSON string containing the values of the class attributes "transcriptionStatus" and "serverName". 
    # Returns the created JSON string. 
    #
    # Return:
    # JSON string containing the values of the class attributes "transcriptionStatus" and "serverName".
    def getTranscriptionStatus(self):
        transcriptionStatus = {"transcriptionStatus":self.transcriptionStatus, 
                               "serverName":self.serverName}
        return json.dumps(transcriptionStatus)

    # Requests the transcript and corresponding row count from static class DataManager. Creates the transcriptionProgressPage 
    # HTML document using the transcript and corresponding row count and returns it as a HTTP response. 
    # 
    # Return:
    # HTTP response containing the transcriptionProgressPage HTML document. 
    def correctionPage(self):
        rowCount, transcript = DataManager.loadTranscript()
        return render_template("correctionPage.html", rows=rowCount, transcriptText=transcript, videoFileName=DataManager.getVideoFileName())
    
    # Receives an HTTP request and checks if it was transmitted using the HTTP method post. Extracts the transcript 
    # from the HTTP request packet and stores it as a PDF Document in the file system. Redirects the client to the downloadPage.
    # 
    # Return: 
    # HTTP redirect to the downloadPage.
    def getCorrectedTranscript(self):
        if request.method == "POST":
            correctedTranscript = request.form.get("transcript")
            DataManager.saveTranscriptAsPDF(correctedTranscript)
        return redirect(url_for("download"))

    # Returns an HTTP response containing the downloadPage HTML document to the client.
    #
    # Return: 
    # HTTP response containing the downloadPage HTML document.
    def downloadPage(self):
        return render_template("downloadPage.html", videoFileName=DataManager.getVideoFileName())
    
    # Sends the transcript PDF Document to the client.
    # 
    # Return: 
    # HTTP response containing the transcript PDF file.  
    def downloadPdf(self):
        return send_file(DataManager.getPdfFilePath(), as_attachment=True)
