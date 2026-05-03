📘 EduGen AI – Intelligent Educational Video Generator
🚀 Overview

EduGen AI is an AI-powered web application that automatically generates educational videos with subtitles and narration based on a given topic and target age group.

The system uses generative AI to create scripts, converts them into speech, and combines them with visuals to produce a complete learning video.


🎯 Key Features:-

🧠 AI Script Generation – Generates age-appropriate educational content

🔊 Text-to-Speech (TTS) – Converts script into audio narration

🎥 Automatic Video Creation – Combines image, audio, and subtitles

📝 Subtitle Integration – Displays script as captions in video

🌐 Web Interface – Simple UI for user input

⚡ End-to-End Automation – From topic → final video in one click


🛠 Tech Stack:-

Frontend: HTML, Tailwind CSS

Backend: Flask (Python)

AI Model: Google Gemini

Text-to-Speech: gTTS (Google Text-to-Speech)

Video Processing: MoviePy

Audio Processing: pydub

Dependencies: ImageMagick




📂 Project Structure:-

EduGenAI/


│

├── app.py                  # Main Flask application

├── audio_gen.py            # Text-to-speech + duration calculation

├── video_creator.py        # Video generation logic

├── script_generator.py     # (Duplicate / optional cleanup)

├── test_imagemagick.py     # Environment check utility

│

├── templates/

│   ├── index.html          # Input form UI

│   └── result.html         # Output display page

│

├── static/

│   ├── audio/              # Generated audio files

│   ├── final_video.mp4     # Output video

│   └── background.jpg      # Video background image

│

├── .env                    # API keys (not included)

└── requirements.txt        # Dependencies




⚙️ How It Works:-

1.User enters topic + age

2.System generates script using AI

3.Script is cleaned for narration

4.Text is converted into speech

5.Audio duration is calculated

6.Video is created with:

  Background image
  
  Subtitles
  
  Audio narration
  

7.Final video is displayed and downloadable



▶️ Installation & Setup:-

1. Clone the repository
git clone https://github.com/your-username/edugen-ai.git
cd edugen-ai

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables
Create a .env file:
GEMINI_API_KEY=your_api_key_here

5. Install ImageMagick
Download and install
Set environment variable:
IMAGEMAGICK_BINARY=path_to_magick.exe

6. Run the application
python app.py
Open browser:
http://127.0.0.1:5000


📸 Usage:-

1.Enter a topic (e.g., Solar System)

2.Select age group

3.Click Generate Video

4.View:
 
  🎥 Video
  
  📝 Script
  
  🔊 Audio

  

⚠️ Limitations:-

1.Uses static background image

2.Limited voice options (gTTS)

3.Requires internet for AI + TTS

4.Basic subtitle styling


🔮 Future Enhancements:-


🎬 Multi-scene dynamic videos

🗣 Advanced voice options (male/female AI voices)

🌍 Multi-language support

📚 Integration with learning platforms


🎨 Animated visuals instead of static images

