import os
import shutil
import pathlib
from fpdf import FPDF
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
    def loadTranscript():
        rowCount = 1
        transcript = ""
        with open(f"{DataManager.filesystemPath}text/transcript.txt") as transcriptFile:
            rowCount = int(transcriptFile.readline())
            transcript = transcriptFile.read()
        return rowCount, transcript

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

    @staticmethod
    def getVideoFilePath():
        return f"{DataManager.filesystemPath}video/{DataManager.videoFileName}"
    
    @staticmethod
    def getVideoFileName():
        return DataManager.videoFileName
    
    @staticmethod 
    def getAudioFilePath():
        return f"{DataManager.filesystemPath}audio/audio.mp3"
    
    @staticmethod
    def getPdfFilePath():
        if len(DataManager.videoFileName.replace('.mp4', '')) > 38:
            return f"{DataManager.filesystemPath}PDF/{DataManager.videoFileName.replace('.mp4', '')[0:38]}_transcription.pdf"
        return f"{DataManager.filesystemPath}PDF/{DataManager.videoFileName.replace('.mp4', '')}_transcription.pdf"    