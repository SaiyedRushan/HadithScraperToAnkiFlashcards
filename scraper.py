import requests
from bs4 import BeautifulSoup
from collections import defaultdict
from anki import *

chapterToHadiths = defaultdict(list)

def scrape_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        current_key = None
        current_values = []
        soup = BeautifulSoup(response.text, 'html.parser')
        allDivs = soup.findAll(True, {'class':['chapter', 'actualHadithContainer']})
        for div in allDivs:

          if 'chapter' in div.get('class', []):
              if current_key and current_values:
                  chapterToHadiths[current_key] = current_values

              chapter = div.find('div', class_='echapno').text.strip() + " - " + div.find('div', class_='englishchapter').text.strip()
              current_key = chapter
              current_values = []

          elif 'actualHadithContainer' in div.get('class', []):
              englishHadith = div.find('div', class_='englishcontainer').text.strip()
              # print(englishHadith + "\n\n")
              current_values.append(englishHadith)

        if current_key and current_values:
            chapterToHadiths[current_key] = current_values
        
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

url = "https://sunnah.com/bukhari/78"
scrape_website(url)
add_hadiths_to_deck(chapterToHadiths)
generate_package()