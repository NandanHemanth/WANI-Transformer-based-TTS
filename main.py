from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from bark import generate_audio
import os
import warnings
from pydub.playback import play

app = FastAPI()

# Set up the template directory to the current directory
templates = Jinja2Templates(directory=os.path.dirname(os.path.abspath(__file__)))

# Mount the 'static' directory from the current directory to serve static files
app.mount("/static", StaticFiles(directory=os.path.dirname(os.path.abspath(__file__))), name="static")

# Render the index.html template
@app.get("/", response_class=HTMLResponse)
async def read_index():
    return templates.TemplateResponse("index.html", {"request": None})


# Your existing WebSocket code (websocket_endpoint) here
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        # Process the received data (e.g., input text)
        # Generate audio using the Bark TTS model
        audio_data = generate_audio(data)

        # Play the audio segment using pydub
        play(audio_data)

        # Send the audio data as bytes to the WebSocket
        await websocket.send_bytes(audio_data)

if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000)

