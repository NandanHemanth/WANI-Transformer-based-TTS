from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
import scipy.io.wavfile as wavfile

# download and load all models
preload_models()

# generate audio from text
text_prompt = """
     Hello, my name is Suno. And, uh — and I like pizza. [laughs] 
     But I also have other interests such as playing tic tac toe.
"""
audio_array = generate_audio(text_prompt)

# specify the output WAV file path
output_file_path = "output_audio.wav"

# save the audio as a WAV file
wavfile.write(output_file_path, SAMPLE_RATE, audio_array)

print("Audio saved successfully as output_audio.wav.")