// Global variable to trigger the timeout function. 
var retry

/*
Fetches the transcription status and uses it to determine if the transcription process is finished. 
If the transcription process is not finished: Sets a delay of 1000 ms and start itself again after. 
If the transcription process is finished: Redirects the client to the correction page. 
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
