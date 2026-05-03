from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=apiKey)

response = client.models.generate_content(
   model="gemini-3-flash-preview",
    contents="Explain about RAG in simple words",
)

print(response.text)