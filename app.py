import os
import re
from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
from video_creator import create_video
from audio_gen import text_to_audio  # Now returns (audio_path, duration)

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
print("🔑 Loaded API key:", GEMINI_API_KEY)

if not GEMINI_API_KEY:
    raise EnvironmentError("❌ GEMINI_API_KEY not found in .env file!")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)
VALID_MODEL_NAME = "models/gemini-1.5-pro-001"
model = genai.GenerativeModel(VALID_MODEL_NAME)

# Flask App
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/generate', methods=['POST'])
def generate():
    topic = request.form.get('topic', '').strip()
    age = request.form.get('age')
    voice = request.form.get('voice')  # Reserved for future use

    print("✅ Received POST request.")
    print(f"🎯 Topic: {topic} | 👶 Age: {age} | 🗣 Voice: {voice}")

    if not topic:
        return render_template('index.html', error="❗ Please enter a topic.")

    try:
        # Step 1: Generate script using Gemini
        prompt = f"Create an engaging and age-appropriate educational video script for a {age}-year-old child on the topic: {topic}."
        response = model.generate_content(prompt)
        script = response.text.strip()

        if not script:
            raise ValueError("❌ Empty script generated.")

        print("📜 Script Generated:\n", script)

        # Step 2: Clean the script for narration
        cleaned_script = clean_text(script)

        # Step 3: Generate audio and get duration
        audio_path, duration_seconds = text_to_audio(cleaned_script)

        # Step 4: Paths
        image_path = os.path.join("static", "background.jpg")
        video_output_path = os.path.join("static", "final_video.mp4")

        # Step 5: Create video with duration synced to audio
        video_path = create_video(
            image_path=image_path,
            audio_path=audio_path,
            output_path=video_output_path,
            text=cleaned_script,
            duration=duration_seconds
        )

        print(f"🔊 Audio Path: {audio_path}")
        print(f"🎥 Video Path: {video_path}")

        return render_template('result.html',
                               video_path=video_path,
                               audio_path=audio_path,
                               script=script)

    except Exception as e:
        print("❌ Error during generation:", e)
        return f"<h1>⚠ Error Occurred</h1><pre>{str(e)}</pre>"

def clean_text(text):
    """
    Clean script for narration (remove unwanted formatting).
    """
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Remove bold markdown
    text = re.sub(r'\(Scene:.*?\)', '', text)     # Remove scene notes
    text = re.sub(r'[•*#>-]', '', text)           # Remove bullets/symbols
    text = re.sub(r'\s{2,}', ' ', text)           # Normalize spaces
    text = re.sub(r'\n+', '. ', text)             # Convert newlines to dots
    text = re.sub(r'[^\w\s.,?!]', '', text)       # Remove non-verbal symbols
    return text.strip()

if __name__ == "__main__":
    app.run(debug=True)
