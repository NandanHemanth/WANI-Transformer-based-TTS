function generateAudio() {
    const inputText = document.getElementById('inputText').value;
    const audioElement = document.getElementById('outputAudio');

    // Send the inputText to the server using socket programming
    // Replace the following code with your socket implementation
    const socket = new WebSocket('ws://127.0.0.1:8000/ws');

    socket.onopen = function (event) {
        socket.send(JSON.stringify({ text: inputText }));
    };

    socket.onmessage = function (event) {
        const audioData = JSON.parse(event.data).audioData;
        const audioBlob = new Blob([new Uint8Array(audioData)], { type: 'audio/wav' });
        const audioURL = URL.createObjectURL(audioBlob);
        audioElement.src = audioURL;
    };
}
