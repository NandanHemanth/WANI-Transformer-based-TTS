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
     In military border communications, brevity and clarity are of utmost importance. To ensure effective and efficient exchanges, soldiers and personnel use concise phrases and acronyms that have become standard in the field. These communication practices enable quick transmission and reception of crucial information, minimizing confusion and misunderstandings.Frequently employed phrases include "Roger that," which is used to acknowledge receipt of a message, and "Copy that," which indicates understanding of the information received. The term "Out" signifies the conclusion of a transmission. These short expressions expedite communication during fast-paced situations, allowing troops to stay focused on their tasks.In addition to phrases, military personnel use acronyms extensively. "SITREP" stands for Situation Report, which provides concise updates on the current status of operations and the overall situation. "OPORD" represents the Operations Order, a comprehensive directive that outlines mission objectives and tactical plans.Another vital acronym is "TGT" for Target. This simplifies the identification and designation of enemy positions or objectives. "HQ" stands for Headquarters, indicating the central command center. "CP" denotes the Command Post, which serves as the local command hub.
Furthermore, "CQB" stands for Close Quarters Battle, referring to combat in confined spaces. "AO" represents the Area of Operations, signifying the designated region where military operations are being conducted. "IED" stands for Improvised Explosive Device, an acronym often encountered in the context of identifying potential threats.Efficient communication at military borders is crucial for coordinating movements, sharing intelligence, and reacting to threats swiftly. By employing these standardized phrases and acronyms, soldiers can maintain situational awareness and respond effectively to evolving situations.In conclusion, military border communications rely on clear and concise language to ensure timely and accurate information exchange. These well-established phrases and acronyms streamline communication, allowing troops to work cohesively and effectively in challenging environments. By adhering to these communication practices, military personnel can enhance operational effectiveness and ensure the safety and success of missions.
"""
audio_segments = trim_text_and_generate_audio(text_prompt)

# save each audio segment as a WAV file
for i, audio_array in enumerate(audio_segments):
    output_file_path = f"output_audio_{i}.wav"
    wavfile.write(output_file_path, SAMPLE_RATE, audio_array)
    print(f"Audio segment {i+1} saved successfully as {output_file_path}.")

    # Play the audio segment
    display(Audio(output_file_path))

print("All audio segments played successfully.")
