import whisper
from moviepy.editor import *
from dataManager import DataManager

# Class that implements functionality to generate a transcript for a video file. 
class TranscriptionService: 
    
    # Initialization of the TranscriptionService Object. Initialize the class attribute "transcript" as an empty string.
    # 
    # Class attributes: 
    # transcript: Stores the generated transcript as a String. 
    def __init__(self):
        self.transcript = ""

    # Use the class methods "extractAudio" and "transcribeVideo" to generate a transcript of a video file.     
    def generateTranscription(self):
        self.extractAudio()
        self.transcribeVideo()

    # Extract the audio from a video file and store it to the file system. 
    def extractAudio(self): 
        video = VideoFileClip(DataManager.getVideoFilePath())
        DataManager.saveAudio(video)

    # Load the transcription model. Generate the transcription for a video and store it in the class attribute "transcript". 
    # Store the transcription in the file system. 
    def transcribeVideo(self):
        # Change used whisper model here:
        model = whisper.load_model("base") #Available models are: tiny, base, small, medium, large
        self.transcript = model.transcribe(DataManager.getAudioFilePath())["text"]
        DataManager.saveTranscript(self.getRowCount(), self.transcript)

    # Calculate the row count of the transcript and return it.
    #
    # Return: 
    # rowCount: The row count of the transcript as an integer. 
    def getRowCount(self):
        rowCount = int(len(self.transcript)/100)+1
        if rowCount > 20: 
            return 20
        return rowCount
