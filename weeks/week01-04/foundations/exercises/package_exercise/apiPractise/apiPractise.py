# import requests
# from twilio.rest import Client
# import json
# from dotenv import load_dotenv
# import os

# Client()
# response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
# print(response.json())

# load_dotenv()

# account_sid = os.getenv("ACCOUNT_SID")
# auth_token = os.getenv("AUTHTOKEN")

# client = Client(account_sid,auth_token)

# message = client.messages.create(
#     body="Hey There!! Hope you are doing well..Syed\n I'm testing",
#     from_= os.getenv("FROMNUM"),
#     to=os.getenv("TONUM"),
# )

# print(message)

# whatsappMessage = client.messages.create(
#     from_= os.getenv("FROM_WHATSAPP"),
#     to= os.getenv("TOWHATSAPP"),
#     content_sid=os.getenv("CONTENTSID"),
#     content_variables=json.dumps({"1": "2 May 2026", "2": "9:43am"}),
# )

# print(whatsappMessage)
