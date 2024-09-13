import whisper
from moviepy.editor import *
from dataManager import DataManager

# Class that implements functionality to generate a transcript for a video file. 
class TranscriptionService: 
    
    # Initialization of the TranscriptionService Object. Initializes the class attribute "transcript" as an empty string.
    # 
    # Class attributes: 
    # transcript: Stores the generated transcript as a String. 
    def __init__(self):
        self.transcript = ""

    # Uses the class methods "extractAudio" and "transcribeVideo" to generate a transcript of a video file.     
    def generateTranscription(self):
        self.extractAudio()
        self.transcribeVideo()

    # Extracts the audio from a video file and stores it to the file system. 
    def extractAudio(self): 
        video = VideoFileClip(DataManager.getVideoFilePath())
        DataManager.saveAudio(video)

    # Loads the transcription model. Generates the transcription for a video and stores it in the class attribute "transcript". 
    # Stores the transcription in the file system. 
    def transcribeVideo(self):
        model = whisper.load_model("tiny") #Available models are: tiny, base, small, medium, large
        self.transcript = model.transcribe(DataManager.getAudioFilePath())["text"]
        DataManager.saveTranscript(self.getRowCount(), self.transcript)

    # Calculates the row count of the transcript and returns it as an integer.
    #
    # Return: 
    # rowCount: the row count of the transcript as an integer. 
    def getRowCount(self):
        rowCount = int(len(self.transcript)/100)+1
        if rowCount > 20: 
            return 20
        return rowCount
