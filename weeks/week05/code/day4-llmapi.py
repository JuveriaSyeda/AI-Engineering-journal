#Building with Chatgpt API

from dotenv import load_dotenv
import os
from groq import Groq
import tiktoken

load_dotenv()

groqAPI_Key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=groqAPI_Key)


# def get_response(prompt,model="llama-3.3-70b-versatile"):
#     message = [
#             {
#             "role":"user",
#             "content":prompt
#             }
#         ]
#     response = client.chat.completions.create(
#             messages = message,
#             model=model,
#             temperature=0
#     )
#     return response.choices[0].message.content

# prompt = "What is the capital of France"
# prompt = "Take the letters in lollipop and reverse them"
# prompt ="""Take the letters in \
# l-o-l-l-i-p-o-p and reverse them"""
# response = get_response(prompt)
# print(response)

# def get_completion_from_messages(messages, 
#                                  model="llama-3.3-70b-versatile", 
#                                  temperature=0, 
#                                  max_tokens=500):
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=temperature, # this is the degree of randomness of the model's output
#         max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
#     )
#     return response.choices[0].message.content

# messages =  [  
# {'role':'system', 
#  'content':"""You are an assistant who
#  responds in the style of Dr Seuss."""},    
# {'role':'user', 
#  'content':"""write me a very short poem
#  about a happy carrot"""},  
# ] 
# messages =  [  
# {'role':'system',
#  'content':'All your responses must be \
# one sentence long.'},    
# {'role':'user',
#  'content':'write me a story about a happy carrot'},  
# ] 
# messages =  [  
# {'role':'system',
#  'content':"""You are an assistant who \
# responds in the style of Dr Seuss. \
# All your responses must be one sentence long."""},    
# {'role':'user',
#  'content':"""write me a story about a happy carrot"""},
# ] 
# response = get_completion_from_messages(messages, temperature=1)
# print(response)

# def get_completion_and_token_count(messages, 
#                                  model="llama-3.3-70b-versatile", 
#                                    temperature=0, 
#                                    max_tokens=500):
    
#     response = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         temperature=temperature, 
#         max_tokens=max_tokens,
#     )
    
#     content = response.choices[0].message.content
#     token_dict = {
# 'prompt_tokens':response.usage.prompt_tokens,
# 'completion_tokens':response.usage.completion_tokens,
# 'total_tokens':response.usage.total_tokens,
#     }

#     return content, token_dict

# messages = [
# {'role':'system', 
#  'content':"""You are an assistant who responds\
#  in the style of Dr Seuss."""},    
# {'role':'user',
#  'content':"""write me a very short poem \ 
#  about a happy carrot"""},  
# ] 
# response, token_dict = get_completion_and_token_count(messages)

# print(response)
# print(token_dict)