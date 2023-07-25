function generateAudio() {
    const inputText = document.getElementById('inputText').value;
    const audioElement = document.getElementById('outputAudio');

    // Connect to the FastAPI WebSocket endpoint
    const socket = new WebSocket('ws://127.0.0.1:8000/ws');

    socket.onopen = function (event) {
        socket.send(inputText);
    };

    socket.onmessage = function (event) {
        // Read the audio data as a Blob
        const audioData = event.data;

        // Create a URL object from the audio data and set it as the audio element's source
        const audioURL = URL.createObjectURL(audioData);
        audioElement.src = audioURL;

        // Play the audio using the audio element
        audioElement.play();
    };
}
