from dotenv import load_dotenv
import os
# from openai import OpenAI
from google import genai
from google.genai import types
import requests

load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")
groqApiKey = os.getenv("GROQ_API_KEY")
client = genai.Client(api_key=apiKey)
#groq
# client = OpenAI(
#     api_key=groqApiKey,
#     base_url="https://api.groq.com/openai/v1"
# )
# response = client.responses.create(
#     input="Explain about LLMs in simple words",
#     model="openai/gpt-oss-20b"
# )
# print(response.output_text)

#get list of all models 
# url = "https://api.groq.com/openai/v1/models"

# headers = {
#     "Authorization": f"Bearer {groqApiKey}",
#     "Content-Type": "application/json"
# }

# response = requests.get(url=url,headers=headers)
# print(response.json())


# googlestudio-gemini

# response = client.models.generate_content(
#    model="gemini-3-flash-preview",
#     contents="Explain about RAG in simple words",
# )

# print(response.text)
# responseThink = client.models.generate_content(
#     model="gemini-3-flash-preview",
#     contents="How does AI work?",
#     config=types.GenerateContentConfig(
#         thinking_config=types.ThinkingConfig(thinking_level="low")
#     ),
# )
# print(responseThink.text)