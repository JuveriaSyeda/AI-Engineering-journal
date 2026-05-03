from dotenv import load_dotenv
import os
from google import genai
from openai import OpenAI


load_dotenv()

apiKey = os.getenv("GEMINI_API_KEY")
groqApiKey = os.getenv("GROQ_API_KEY")
# client = genai.Client(api_key=apiKey)

# response = client.models.generate_content(
#    model="gemini-3-flash-preview",
#     contents="Explain about RAG in simple words",
# )

# print(response.text)

client = OpenAI(
    api_key=groqApiKey,
    base_url="https://api.groq.com/openai/v1"
)
response = client.responses.create(
    input="Explain about LLMs in simple words",
    model="openai/gpt-oss-20b"
)
print(response.output_text)