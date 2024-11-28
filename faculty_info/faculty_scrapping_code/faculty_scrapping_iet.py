from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

driver = webdriver.Firefox()

with open('/home/abhay/my_projects/ps2_chatbot/faculty_profile_links_management.txt', 'r') as file:
    urls = [line.strip() for line in file.readlines()]

output_directory = "faculty_info_management"
os.makedirs(output_directory, exist_ok=True)

def extract_faculty_name(url):
    name_part = url.rstrip('/').split('/')[-1]
    faculty_name = name_part.replace('-', ' ').title()
    return faculty_name

def extract_faculty_info(url):
    driver.get(url)
    time.sleep(3)

    plus_buttons = driver.find_elements(By.CLASS_NAME, 'elementor-toggle-icon')
    for button in plus_buttons:
        button.click()

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    faculty_info = {}

    education_section = soup.find('div', {'data-widget_type': 'text-editor.default', 'data-id': '3526a94'})
    if education_section:
        faculty_info['Education'] = education_section.get_text(strip=True)

    experience_section = soup.find('div', {'data-widget_type': 'text-editor.default', 'data-id': 'a37b467'})
    if experience_section:
        faculty_info['Experience'] = experience_section.get_text(strip=True)

    teaching_interests_section = soup.find('div', {'data-title': 'teaching-interests'})
    if teaching_interests_section:
        faculty_info['Teaching Interests'] = teaching_interests_section.find_next('ul').get_text(separator='\n', strip=True)

    research_interests_section = soup.find('div', {'data-title': 'research-interests'})
    if research_interests_section:
        faculty_info['Research Interests'] = research_interests_section.find_next('ul').get_text(separator='\n', strip=True)

    honors_awards_section = soup.find('div', {'data-title': 'honours-awards-and-affiliations'})
    if honors_awards_section:
        faculty_info['Honors, Awards, and Affiliations'] = honors_awards_section.find_next('ul').get_text(separator='\n', strip=True)

    publications_section = soup.find('div', {'data-title': 'selected-publications'})
    if publications_section:
        faculty_info['Selected Publications'] = publications_section.find_next('ul').get_text(separator='\n', strip=True)

    return faculty_info

for url in urls:
    faculty_name = extract_faculty_name(url)
    print(f"Extracting info for: {faculty_name}")
    
    faculty_data = extract_faculty_info(url)

    file_name = f"{faculty_name.replace(' ', '_')}.txt"
    file_path = os.path.join(output_directory, file_name)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Faculty Name: {faculty_name}\n\n")
        for section, content in faculty_data.items():
            file.write(f"--- {section} ---\n")
            file.write(f"{content}\n\n")

    print(f"Data for {faculty_name} saved to {file_path}")

driver.quit()

print("Extraction completed.")
