import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Get the Gemini API key from environment
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

# Check if key is loaded properly
if not GEMINI_API_KEY:
    raise ValueError("❌ Gemini API Key not found. Please check your .env file.")

# Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Use the model
model = genai.GenerativeModel("models/gemini-pro")

def generate_script(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("❌ Error generating script:", e)  # <-- this will print the real issue
        return None