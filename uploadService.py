import filetype
from dataManager import DataManager

# Class that implements functionality to check if a file was uploaded and has the correct file format. 
class UploadService: 
    
    # Initialization of the UploadService Object. Takes an HTTP request packet, 
    # checks if it was transmitted using the HTTP method post and extracts the FileStorage
    # Object and the filename string from it, and stores them in the Object's attributes.
    #
    # Class attributes: 
    # uploadedFile: Stores the uploaded file as a FileStorage Object. 
    # uploadedFileName: Stores the name of the uploaded file as a string. 
    #
    # Input:
    # request: A HTTP request packet.
    def __init__(self, request):
        self.uploadedFileName = ""
        if request.method == 'POST': 
            self.uploadedFile = request.files['file']
            self.uploadedFileName = self.uploadedFile.filename

    # Uses the class attribute "uploadedFileName" to determine if a file was uploaded. 
    #
    # Return:
    # Boolean indicating if a file was uploaded or not. 
    def fileNotUploaded(self):
        if self.uploadedFileName == "":
            return True
        return False
    
    # Saves the uploaded file to the file system. Checks if the file has the correct file format (MP4). 
    # If the file has the wrong file format: Deletes the file and returns false. 
    # If the file has the correct format: Returns true.     
    #
    # Return: 
    # Boolean indicating if the file has the correct file format.
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
    