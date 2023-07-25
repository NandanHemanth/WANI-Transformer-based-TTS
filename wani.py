from bark import SAMPLE_RATE, generate_audio, preload_models
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

# generate audio from text and return audio data as bytes
def generate_audio_bytes(text):
    audio_segments = trim_text_and_generate_audio(text)
    audio_data_list = []

    for i, audio_array in enumerate(audio_segments):
        with io.BytesIO() as buf:
            wavfile.write(buf, SAMPLE_RATE, audio_array)
            audio_data_list.append(buf.getvalue())

    return audio_data_list

# save each audio segment as a WAV file
for i, audio_array in enumerate(audio_segments):
    output_file_path = f"output_audio_{i}.wav"
    wavfile.write(output_file_path, SAMPLE_RATE, audio_array)
    print(f"Audio segment {i+1} saved successfully as {output_file_path}.")

    # Play the audio segment using pydub
    play(output_file_path)

print("All audio segments played successfully.")
