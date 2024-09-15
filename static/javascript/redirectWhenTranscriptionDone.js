// Global variable to trigger the timeout function. 
var retry

/*
Fetche the transcription status and use it to determine if the transcription process is finished. 
If the transcription process is not finished: Set a delay of 1000 ms and start redirectWhenTranscriptionDone function again after. 
If the transcription process is finished: Redirect the client to the correction page. 
*/
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

// Initial invocation of the redirectWhenTranscriptionDone function. 
redirectWhenTranscriptionDone()
