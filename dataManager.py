import os
import shutil
import pathlib

class DataManager:
    filesystemPath = f"{pathlib.Path(__file__).parent.resolve()}/Data/"
    videoFileName = ""

    @staticmethod 
    def initailizeFilesystem():
        if not os.path.exists(DataManager.filesystemPath):
            os.mkdir(DataManager.filesystemPath)
            os.mkdir(f"{DataManager.filesystemPath}audio")
            os.mkdir(f"{DataManager.filesystemPath}PDF")
            os.mkdir(f"{DataManager.filesystemPath}text")
            os.mkdir(f"{DataManager.filesystemPath}video")

    @staticmethod 
    def resetFileSystem():
        DataManager.videoFileName = ""
        shutil.rmtree(DataManager.filesystemPath[:-1])
        os.mkdir(DataManager.filesystemPath[:-1])
        os.mkdir(f"{DataManager.filesystemPath}audio")
        os.mkdir(f"{DataManager.filesystemPath}PDF")
        os.mkdir(f"{DataManager.filesystemPath}text")
        os.mkdir(f"{DataManager.filesystemPath}video")
    
    @staticmethod
    def saveUploadedFile(file):
        DataManager.videoFileName = file.filename 
        file.save(DataManager.getVideoFilePath())

    @staticmethod
    def removeUploadedFile():
        os.remove(DataManager.getVideoFilePath())
        DataManager.videoFileName = ""

    @staticmethod
    def getVideoFilePath():
        return f"{DataManager.filesystemPath}video/{DataManager.videoFileName}"
    