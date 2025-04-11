from gtts import gTTS
from pydub import AudioSegment
import os
import uuid

def text_to_audio(script_text):
    # Ensure output directory exists
    output_dir = "static/audio"
    os.makedirs(output_dir, exist_ok=True)

    # Create a unique filename
    filename = os.path.join(output_dir, f"audio_{uuid.uuid4().hex}.mp3")

    # Generate TTS audio
    tts = gTTS(text=script_text.strip(), lang='en')
    tts.save(filename)

    # Load the audio file to get its duration (in seconds)
    audio = AudioSegment.from_file(filename)
    duration_seconds = len(audio) / 1000.0  # convert milliseconds to seconds

    return filename, duration_seconds
