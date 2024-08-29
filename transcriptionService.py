import whisper
from moviepy.editor import *
from dataManager import DataManager

class TranscriptionService: 
    def __init__(self):
        self.transcript = ""
        
    def generateTranscription(self):
        self.extractAudio()
        self.transcribeVideo()

    def extractAudio(self): 
        video = VideoFileClip(DataManager.getVideoFilePath())
        DataManager.saveAudio(video)

    def transcribeVideo(self):
        model = whisper.load_model("tiny") #tiny, base, small, medium, large
        self.transcript = model.transcribe(DataManager.getAudioFilePath())["text"]
        DataManager.saveTranscript(self.getRowCount(), self.transcript)

    def getRowCount(self):
        rowCount = int(len(self.transcript)/100)+1
        if rowCount > 20: 
            return 20
        return rowCount
