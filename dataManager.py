import os
import shutil
import pathlib
from moviepy.editor import *

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
    def saveAudio(audio : VideoFileClip):
        audio.audio.write_audiofile(DataManager.getAudioFilePath())

    @staticmethod 
    def saveTranscript(rowCount, transcript):
        with open(f"{DataManager.filesystemPath}text/transcript.txt", "w") as transcriptFile:
            transcriptFile.write(f"{rowCount}\n")
            transcriptFile.write(transcript)

    @staticmethod
    def getVideoFilePath():
        return f"{DataManager.filesystemPath}video/{DataManager.videoFileName}"
    
    @staticmethod
    def getVideoFileName():
        return DataManager.videoFileName
    
    @staticmethod 
    def getAudioFilePath():
        return f"{DataManager.filesystemPath}audio/audio.mp3"
    