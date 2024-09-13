import os
import shutil
import pathlib
from fpdf import FPDF
from moviepy.editor import *
from werkzeug import datastructures

# Static class that implements functionality to store and retrieve data from the file system. 
class DataManager:
    
    # The path to the directory structure the system uses to store data.
    filesystemPath = f"{pathlib.Path(__file__).parent.resolve()}/Data/"

    # The name of the currently processed video file.
    videoFileName = ""

    # Checks if the directory structure that the system needs to store data is present and creates it if not. 
    @staticmethod 
    def initailizeFilesystem():
        if not os.path.exists(DataManager.filesystemPath):
            os.mkdir(DataManager.filesystemPath)
            os.mkdir(f"{DataManager.filesystemPath}audio")
            os.mkdir(f"{DataManager.filesystemPath}PDF")
            os.mkdir(f"{DataManager.filesystemPath}text")
            os.mkdir(f"{DataManager.filesystemPath}video")

    # Removes all data that the System stored in the filesystem. Also resets the "videoFileName" attribute to an empty string. 
    @staticmethod 
    def resetFileSystem():
        DataManager.videoFileName = ""
        shutil.rmtree(DataManager.filesystemPath[:-1])
        os.mkdir(DataManager.filesystemPath[:-1])
        os.mkdir(f"{DataManager.filesystemPath}audio")
        os.mkdir(f"{DataManager.filesystemPath}PDF")
        os.mkdir(f"{DataManager.filesystemPath}text")
        os.mkdir(f"{DataManager.filesystemPath}video")
    
    # Takes a file as an "FileStorage"-Object and stores it in the video file's directory.
    # 
    # Input: 
    # file: FileStorage-Object.  
    @staticmethod
    def saveUploadedFile(file : datastructures.file_storage.FileStorage):
        DataManager.videoFileName = file.filename 
        file.save(DataManager.getVideoFilePath())

    # Deletes the current file from the video file's directory. Sets the "videoFileName" attribute to an empty string.
    @staticmethod
    def removeUploadedFile():
        os.remove(DataManager.getVideoFilePath())
        DataManager.videoFileName = ""

    # Takes a video file as an "VideoFileClip"-Object and stores the audio data from this video file in the audio file's directory.
    #
    # Input: 
    # video: VideoFileClip-Object.
    @staticmethod    
    def saveAudio(video : VideoFileClip):
        video.audio.write_audiofile(DataManager.getAudioFilePath())

    # Saves a Transcript and its corresponding row count as a text file in the text file directory.
    #
    # Input: 
    # rowCount: The row count of the transcript as an integer. 
    # transcript: The transcript as a string. 
    @staticmethod 
    def saveTranscript(rowCount, transcript):
        with open(f"{DataManager.filesystemPath}text/transcript.txt", "w") as transcriptFile:
            transcriptFile.write(f"{rowCount}\n")
            transcriptFile.write(transcript)

    # Loads a transcript and its row count from the text file directory and returns this data. 
    #
    # Return:
    # rowCount: The row count of the transcript as an integer. 
    # transcript: The transcript as a string.
    @staticmethod 
    def loadTranscript():
        rowCount = 1
        transcript = ""
        with open(f"{DataManager.filesystemPath}text/transcript.txt") as transcriptFile:
            rowCount = int(transcriptFile.readline())
            transcript = transcriptFile.read()
        return rowCount, transcript

    # Takes a transcript as a string, formats it as a PDF file and stores it in the PDF file's directory.
    #
    # Input:  
    # transcript: The transcript as a string. 
    @staticmethod 
    def saveTranscriptAsPDF(transcript):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font(family = "Arial", style = "B", size = 16)

        if len(DataManager.videoFileName) > 35:
            pdfTitle = f"Transkript des Videos {DataManager.videoFileName[0:35]}...\n"
        else:    
            pdfTitle = f"Transkript des Videos {DataManager.videoFileName}\n"

        pdf.cell(w = 0, txt=pdfTitle, ln=1, align="C")
        pdf.cell(w=0, h=10, txt="", ln=1)
        pdf.set_font(family="", style="", size = 12)
        pdf.multi_cell(w = 0, h = 5, txt = transcript)
        pdf.output(DataManager.getPdfFilePath())

    # Returns the path of the video file's directory.
    # 
    # Return:
    # A string containing the path of the video file's directory.
    @staticmethod
    def getVideoFilePath():
        return f"{DataManager.filesystemPath}video/{DataManager.videoFileName}"
    
    # Returns a string containing the name of the currently processed video file.
    # 
    # Return:
    # A string containing the name of the currently processed video file. 
    @staticmethod
    def getVideoFileName():
        return DataManager.videoFileName
    
    # Returns the path of the audio file's directory.
    # 
    # Return:
    # A string containing the path of the audio file's directory.
    @staticmethod 
    def getAudioFilePath():
        return f"{DataManager.filesystemPath}audio/audio.mp3"
    
    # Returns the path of the PDF file's directory.
    # 
    # Return:
    # A string containing the path of the PDF file's directory.
    @staticmethod
    def getPdfFilePath():
        if len(DataManager.videoFileName.replace('.mp4', '')) > 38:
            return f"{DataManager.filesystemPath}PDF/{DataManager.videoFileName.replace('.mp4', '')[0:38]}_transcription.pdf"
        return f"{DataManager.filesystemPath}PDF/{DataManager.videoFileName.replace('.mp4', '')}_transcription.pdf"  
      