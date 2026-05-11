import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()
groqAPI_Key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groqAPI_Key)

#scrapping
url = "https://docs.astral.sh/uv/"
# url = "https://groq.com"

headers = {
    "User-Agent": "Chrome/136.0.0.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Page fetched successfully!")
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
else:
    print("Failed to fetch page:", response.status_code)



def get_response(prompt,model="llama-3.3-70b-versatile"):
    message = [
        {
            "role":"system",
            "content":"You are a helpful summarizer."
            },
            {
            "role":"user",
            "content":prompt
            }
        ]
    response = client.chat.completions.create(
            messages = message,
            model=model,
            temperature=0
    )
    return response.choices[0].message.content

prompt = f"Summarize the webpage content in bullet points. {text}"

finalResponse = get_response(prompt)
print(finalResponse)
