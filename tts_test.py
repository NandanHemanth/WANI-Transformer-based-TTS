from bark import SAMPLE_RATE, generate_audio, preload_models
import scipy.io.wavfile as wavfile
import io
from pydub.playback import play
import pandas as pd
import time
import torch

# Download and load all models
preload_models()

# Function to generate audio from text and return audio data as bytes
def generate_audio_bytes(text, speaker_id=None, history_prompt=None, device=None):
    audio_array = generate_audio(text, speaker_id=speaker_id, history_prompt=history_prompt, device=device)
    with io.BytesIO() as buf:
        wavfile.write(buf, SAMPLE_RATE, audio_array)
        audio_data = buf.getvalue()

    return audio_data

# Read sentences from the Excel sheet
df = pd.read_excel("test_text.xlsx", sheet_name="Sheet1")

# Check if GPU is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("GPU is available. Using GPU for TTS.")
else:
    device = torch.device("cpu")
    print("No GPU found. Using CPU for TTS.")

# Iterate through each row and generate audio for each sentence
for index, row in df.iterrows():
    english_sentence = row["English"]
    hindi_sentence = row["Hindi"]
    chinese_sentence = row["Chinese"]

    print(f"Processing Sentence {index + 1}...")
    
    # Generate audio for each sentence in English, Hindi, and Chinese
    english_audio = generate_audio_bytes(english_sentence, speaker_id="en_speaker_1", device=device)
    hindi_audio = generate_audio_bytes(hindi_sentence, speaker_id="hi_speaker_1", device=device)
    chinese_audio = generate_audio_bytes(chinese_sentence, speaker_id="zh_speaker_1", device=device)

    # Save audio as WAV files
    wavfile.write(f"output_audio_english_{index + 1}.wav", SAMPLE_RATE, english_audio)
    wavfile.write(f"output_audio_hindi_{index + 1}.wav", SAMPLE_RATE, hindi_audio)
    wavfile.write(f"output_audio_chinese_{index + 1}.wav", SAMPLE_RATE, chinese_audio)

    print(f"Audio files for Sentence {index + 1} saved successfully.")

print("All audio segments generated and saved successfully.")
