import requests
from bs4 import BeautifulSoup
import os

def format_text_for_rag(content):
    formatted_text = ""
    
    for elem in content:
        if elem.name == 'h1' or elem.name == 'h4':
            formatted_text += f"\n\n# {elem.text.strip()} #\n"
        elif elem.name == 'p':
            formatted_text += f"\n{elem.text.strip()}\n"
        elif elem.name == 'ul':
            for li in elem.find_all('li'):
                formatted_text += f"- {li.text.strip()}\n"
        else:
            formatted_text += f"{elem.text.strip()}\n"
    return formatted_text

def scrape_and_save(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    main_content = soup.find('div', class_='main-wrapper')
    
    if not main_content:
        print(f"Main content not found for {url}")
        return
    
    formatted_content = format_text_for_rag(main_content.find_all(['h1', 'h4', 'p', 'ul']))
    
    file_name = url.strip('/').split('/')[-1] + ".txt"
    file_path = os.path.join('./scraped_files', file_name)
    
    os.makedirs('./scraped_files', exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)
    
    print(f"Content from {url} saved to {file_path}")

urls = [
    "https://jklu.edu.in/studentlife/media-club/",
    "https://jklu.edu.in/studentlife/white-spacedesign-club/",
    "https://jklu.edu.in/studentlife/quiz-club/",
    "https://jklu.edu.in/studentlife/muse-ink-literary-club/",
    "https://jklu.edu.in/studentlife/community-development-club/",
    "https://jklu.edu.in/studentlife/applied-robotics-club/",
    "https://jklu.edu.in/studentlife/coding-club/",
    "https://jklu.edu.in/studentlife/competitive-programming-club/",
    "https://jklu.edu.in/studentlife/nakshatrathe-astronomy-club/",
    "https://jklu.edu.in/studentlife/business-finanace-club/",
    "https://jklu.edu.in/studentlife/stepper-squaddance-club/",
    "https://jklu.edu.in/studentlife/music-club/",
    "https://jklu.edu.in/studentlife/drama-club-jklu/",
    "https://jklu.edu.in/studentlife/house-of-arts/",


    
]

for url in urls:
    scrape_and_save(url)
