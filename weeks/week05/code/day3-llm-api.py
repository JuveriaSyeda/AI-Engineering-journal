from dotenv import load_dotenv
import os
from groq import Groq
from redlines import Redlines


load_dotenv()
apiKey = os.getenv("GROQ_API_KEY")

client = Groq(api_key=apiKey)

def get_response(prompt,model="llama-3.3-70b-versatile"):
    message = [
            {
            "role":"user",
            "content":prompt
            }
        ]
    response = client.chat.completions.create(
         messages=message,
         model=model,
         temperature=0
    )
    return response.choices[0].message.content

# lamp_review = """
# Needed a nice lamp for my bedroom, and this one had \
# additional storage and not too high of a price point. \
# Got it fast.  The string to our lamp broke during the \
# transit and the company happily sent over a new one. \
# Came within a few days as well. It was easy to put \
# together.  I had a missing part, so I contacted their \
# support and they very quickly got me the missing piece! \
# Lumina seems to me to be a great company that cares \
# about their customers and products!!
# """

# # Sentiment (positive/negative)
# prompt = f"""
# What is the sentiment of the following product review, 
# which is delimited with triple backticks?

# Review text: '''{lamp_review}'''
# """
# prompt = f"""
# What is the sentiment of the following product review, 
# which is delimited with triple backticks?

# Give your answer as a single word, either "positive" \
# or "negative".

# Review text: '''{lamp_review}'''
# """

## Identify types of emotions

# prompt = f"""
# Identify a list of emotions that the writer of the \
# following review is expressing. Include no more than \
# five items in the list. Format your answer as a list of \
# lower-case words separated by commas.

# Review text: '''{lamp_review}'''
# """

## Identify anger
# prompt = f"""
# Is the writer of the following review expressing anger?\
# The review is delimited with triple backticks. \
# Give your answer as either yes or no.

# Review text: '''{lamp_review}'''
# """

# Extract product and company name from customer reviews
# prompt = f"""
# Identify the following items from the review text: 
# - Item purchased by reviewer
# - Company that made the item

# The review is delimited with triple backticks. \
# Format your response as a JSON object with \
# "Item" and "Brand" as the keys. 
# If the information isn't present, use "unknown" \
# as the value.
# Make your response as short as possible.
  
# Review text: '''{lamp_review}'''
# """

# Doing multiple tasks at once
# prompt = f"""
# Identify the following items from the review text: 
# - Sentiment (positive or negative)
# - Is the reviewer expressing anger? (true or false)
# - Item purchased by reviewer
# - Company that made the item

# The review is delimited with triple backticks. \
# Format your response as a JSON object with \
# "Sentiment", "Anger", "Item" and "Brand" as the keys.
# If the information isn't present, use "unknown" \
# as the value.
# Make your response as short as possible.
# Format the Anger value as a boolean.

# Review text: '''{lamp_review}'''
# """

## Inferring topics
# story = """
# In a recent survey conducted by the government, 
# public sector employees were asked to rate their level 
# of satisfaction with the department they work at. 
# The results revealed that NASA was the most popular 
# department with a satisfaction rating of 95%.

# One NASA employee, John Smith, commented on the findings, 
# stating, "I'm not surprised that NASA came out on top. 
# It's a great place to work with amazing people and 
# incredible opportunities. I'm proud to be a part of 
# such an innovative organization."

# The results were also welcomed by NASA's management team, 
# with Director Tom Johnson stating, "We are thrilled to 
# hear that our employees are satisfied with their work at NASA. 
# We have a talented and dedicated team who work tirelessly 
# to achieve our goals, and it's fantastic to see that their 
# hard work is paying off."

# The survey also revealed that the 
# Social Security Administration had the lowest satisfaction 
# rating, with only 45% of employees indicating they were 
# satisfied with their job. The government has pledged to 
# address the concerns raised by employees in the survey and 
# work towards improving job satisfaction across all departments.
# """
# prompt = f"""
# Determine five topics that are being discussed in the \
# following text, which is delimited by triple backticks.

# Make each item one or two words long. 

# Format your response as a list of items separated by commas.

# Text sample: '''{story}'''
# """



#Transforming
# prompt = f"""
# Translate the following English text to Spanish: \ 
# ```Hi, I would like to order a blender```
# """

# prompt = f"""
# Tell me which language this is: 
# ```Combien coûte le lampadaire?```
# """

# prompt = f"""
# Translate the following  text to French and Spanish
# and English pirate: \
# ```I want to order a basketball```
# """

# prompt = f"""
# Translate the following text to Spanish in both the \
# formal and informal forms: 
# 'Would you like to order a pillow?'
# """

# user_messages = [
#   "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
#   "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
#   "Il mio mouse non funziona",                                 # My mouse is not working
#   "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
#   "我的屏幕在闪烁"                                               # My screen is flashing
# ] 
# for issue in user_messages:
#     prompt = f"Tell me what language this is: ```{issue}```"
#     lang = get_completion(prompt)
#     print(f"Original message ({lang}): {issue}")

#     prompt = f"""
#     Translate the following  text to English \
#     and Korean: ```{issue}```
#     """


#Tone Transformation
# prompt = f"""
# Translate the following from slang to a business letter: 
# 'Dude, This is Joe, check out this spec on this standing lamp.'
# """
# data_json = { "resturant employees" :[ 
#     {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
#     {"name":"Bob", "email":"bob32@gmail.com"},
#     {"name":"Jai", "email":"jai87@gmail.com"}
# ]}

# prompt = f"""
# Translate the following python dictionary from JSON to an HTML 
# table with column headers and title: {data_json}
# """



#Spellcheck/Grammar check.
# text = [ 
#   "The girl with the black and white puppies have a ball.",  # The girl has a ball.
#   "Yolanda has her notebook.", # ok
#   "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
#   "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
#   "Your going to need you’re notebook.",  # Homonyms
#   "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
#   "This phrase is to cherck chatGPT for speling abilitty"  # spelling
# ]
# for t in text:
#     prompt = f"""Proofread and correct the following text
#     and rewrite the corrected version. If you don't find
#     and errors, just say "No errors found". Don't use 
#     any punctuation around the text:
#     ```{t}```"""

# text = f"""
# Got this for my daughter for her birthday cuz she keeps taking 
# mine from my room.  Yes, adults also like pandas too.  She takes 
# it everywhere with her, and it's super soft and cute.  One of the 
# ears is a bit lower than the other, and I don't think that was 
# designed to be asymmetrical. It's a bit small for what I paid for it 
# though. I think there might be other options that are bigger for 
# the same price.  It arrived a day earlier than expected, so I got 
# to play with it myself before I gave it to my daughter.
# """
# prompt = f"proofread and correct this review: ```{text}```"


#Expanding

# sentiment = "negative"

# review for a blender
# review = f"""
# So, they still had the 17 piece system on seasonal \
# sale for around $49 in the month of November, about \
# half off, but for some reason (call it price gouging) \
# around the second week of December the prices all went \
# up to about anywhere from between $70-$89 for the same \
# system. And the 11 piece system went up around $10 or \
# so in price also from the earlier sale price of $29. \
# So it looks okay, but if you look at the base, the part \
# where the blade locks into place doesn’t look as good \
# as in previous editions from a few years ago, but I \
# plan to be very gentle with it (example, I crush \
# very hard items like beans, ice, rice, etc. in the \ 
# blender first then pulverize them in the serving size \
# I want in the blender then switch to the whipping \
# blade for a finer flour, and use the cross cutting blade \
# first when making smoothies, then use the flat blade \
# if I need them finer/less pulpy). Special tip when making \
# smoothies, finely cut and freeze the fruits and \
# vegetables (if using spinach-lightly stew soften the \ 
# spinach then freeze until ready for use-and if making \
# sorbet, use a small to medium sized food processor) \ 
# that you plan to use that way you can avoid adding so \
# much ice if at all-when making your smoothie. \
# After about a year, the motor was making a funny noise. \
# I called customer service but the warranty expired \
# already, so I had to buy another one. FYI: The overall \
# quality has gone done in these types of products, so \
# they are kind of counting on brand recognition and \
# consumer loyalty to maintain sales. Got it in about \
# two days.
# """
# prompt = f"""
# You are a customer service AI assistant.
# Your task is to send an email reply to a valued customer.
# Given the customer email delimited by ```, \
# Generate a reply to thank the customer for their review.
# If the sentiment is positive or neutral, thank them for \
# their review.
# If the sentiment is negative, apologize and suggest that \
# they can reach out to customer service. 
# Make sure to use specific details from the review.
# Write in a concise and professional tone.
# Sign the email as `AI customer agent`.
# Customer review: ```{review}```
# Review sentiment: {sentiment}
# """

# prompt = f"""
# You are a customer service AI assistant.
# Your task is to send an email reply to a valued customer.
# Given the customer email delimited by ```, \
# Generate a reply to thank the customer for their review.
# If the sentiment is positive or neutral, thank them for \
# their review.
# If the sentiment is negative, apologize and suggest that \
# they can reach out to customer service. 
# Make sure to use specific details from the review.
# Write in a concise and professional tone.
# Sign the email as `AI customer agent`.
# Customer review: ```{review}```
# Review sentiment: {sentiment}
# """


# response = get_response(prompt=prompt)
# print(response)
# diff = Redlines(text,response)
# print(diff.output_markdown)