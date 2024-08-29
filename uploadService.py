import filetype
from dataManager import DataManager

class UploadService: 
    def __init__(self, request):
        self.uploadedFileName = ""
        if request.method == 'POST': 
            self.uploadedFile = request.files['file']
            self.uploadedFileName = self.uploadedFile.filename

    def fileNotUploaded(self):
        if self.uploadedFileName == "":
            return True
        return False
    
    def validateFileFormat(self):
        DataManager.saveUploadedFile(self.uploadedFile)
        
        recognizedFileFormat = filetype.guess(DataManager.getVideoFilePath())

        if recognizedFileFormat == None:
            DataManager.removeUploadedFile()
            return False
        
        if recognizedFileFormat.extension != "mp4":
            DataManager.removeUploadedFile()
            return False
        return True
    