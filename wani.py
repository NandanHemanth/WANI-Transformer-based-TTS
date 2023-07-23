from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
import scipy.io.wavfile as wavfile

# download and load all models
preload_models()

def trim_text_and_generate_audio(text):
    max_text_length = 1024
    words = text.split()
    current_text = ""
    audio_segments = []
    
    for word in words:
        if len(current_text) + len(word) <= max_text_length:
            current_text += word + " "
        else:
            audio_array = generate_audio(current_text.strip())
            audio_segments.append(audio_array)
            current_text = word + " "
    
    if current_text.strip():
        audio_array = generate_audio(current_text.strip())
        audio_segments.append(audio_array)

    return audio_segments

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_segments = trim_text_and_generate_audio(text_prompt)

# save each audio segment as a WAV file
for i, audio_array in enumerate(audio_segments):
    output_file_path = f"output_audio_{i}.wav"
    wavfile.write(output_file_path, SAMPLE_RATE, audio_array)
    print(f"Audio segment {i+1} saved successfully as {output_file_path}.")
