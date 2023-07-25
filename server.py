from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from bark import generate_audio
import os
from fastapi import FastAPI, WebSocket
import scipy.io.wavfile as wavfile
from pydub.playback import play

app = FastAPI()

# Set up the template directory to the current directory
templates = Jinja2Templates(directory=os.path.dirname(os.path.abspath(__file__)))

# Mount the 'static' directory from the current directory to serve static files
app.mount("/static", StaticFiles(directory=os.path.dirname(os.path.abspath(__file__))), name="static")

# Your existing WebSocket code (websocket_endpoint) here
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        # Process the received data (e.g., input text)
        # Generate audio using the Bark TTS model
        audio_data = generate_audio(data)

        # Send the audio data back to the client
        await websocket.send_bytes(audio_data)

if __name__ == "__main__":
    # Start the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
