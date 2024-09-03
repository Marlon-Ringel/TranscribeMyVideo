var retry

async function redirectWhenTranscriptionDone() {
    let status;
  
    try {
        const result = await fetch("/transcription_status");
        status = await result.json();
    } catch (error) {
        console.error("Error: ", error);
    }

    if(status.transcriptionStatus == "done") {
        window.location.replace(status.serverName+"correct_transcript")
    }
    else if(window.location.href == status.serverName+"transcription_process"){
        retry = setTimeout(redirectWhenTranscriptionDone, 1000)
    }     
}

redirectWhenTranscriptionDone()
