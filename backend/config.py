import os
from google import genai

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Set it as an environment variable before "
        "starting the Paper Checker backend."
    )

# Initialize the client once and reuse it across the grading pipeline.
client = genai.Client(api_key=API_KEY)

# Model configuration
MODEL_NAME = "gemini-2.5-flash"
