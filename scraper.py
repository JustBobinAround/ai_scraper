import requests
from bs4 import BeautifulSoup

zip = input("Enter a zip link: ")

response = requests.get(f"https://www.redfin.com/zipcode/{zip}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    homes = soup.find_all(class_='homecardv2')

    print(f"len:{len(homes)}")
    for home in homes:
        link = home.find('a')['href']
        print(f'Link: https://www.redfin.com{link}')
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')


