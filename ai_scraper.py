import os
import openai
import requests
from bs4 import BeautifulSoup

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

def generate_coverletter(user_prompt):
    system_prompt = "Your task is to create a wholesaling coverletter of a property for a client\
    based on the information the user provides."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )
    return response['choices'][0]['message']['content']

print("Ai letter maker:")
url = input("Enter a redfin link: ")
property_info = ""
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all(class_='alongTheRail')

    print(f"len:{len(articles)}")
    for article in articles:
        for span in article.find_all('span'):
            property_info += span.text + "\n"
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')

coverletter = generate_summary(property_info)
print(coverletter)
