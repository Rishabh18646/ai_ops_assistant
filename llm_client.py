import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load Gemini API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_llm(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")   # you can also use gemini-1.5-pro
    response = model.generate_content(prompt)
    return response.text
