from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

driver = webdriver.Firefox()

url = "https://jklu.edu.in/design/permanent-faculty/#yash"

driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

faculties = []

faculty_sections = soup.find_all('div', class_='elementor-widget-wrap elementor-element-populated')

for section in faculty_sections:
    faculty = {}
    
    name = section.find('h4', class_='elementor-heading-title elementor-size-default')
    if name:
        faculty['Name'] = name.get_text(strip=True)
    
    title = section.find('h5', class_='elementor-heading-title elementor-size-default')
    if title:
        faculty['Title'] = title.get_text(strip=True)
    
    qualifications = section.find('h6', class_='elementor-heading-title elementor-size-default')
    if qualifications:
        faculty['Qualifications'] = qualifications.get_text(strip=True)
    
    bio = ""
    bio_paragraphs = section.find_all('p')
    for paragraph in bio_paragraphs:
        bio += paragraph.get_text(separator=' ', strip=True) + " "

    bio_list = section.find_all('ul')
    for ul in bio_list:
        for li in ul.find_all('li'):
            bio += "- " + li.get_text(separator=' ', strip=True) + " "
    
    if bio:
        faculty['Bio'] = bio.strip()
    
    faculties.append(faculty)

for faculty in faculties:
    print("Faculty Name:", faculty.get('Name', 'N/A'))
    print("Title:", faculty.get('Title', 'N/A'))
    print("Qualifications:", faculty.get('Qualifications', 'N/A'))
    print("Bio:", faculty.get('Bio', 'N/A'))
    print("-" * 80)

with open("faculty_info.txt", "w", encoding="utf-8") as f:
    for faculty in faculties:
        f.write(f"Faculty Name: {faculty.get('Name', 'N/A')}\n")
        f.write(f"Title: {faculty.get('Title', 'N/A')}\n")
        f.write(f"Qualifications: {faculty.get('Qualifications', 'N/A')}\n")
        f.write(f"Bio: {faculty.get('Bio', 'N/A')}\n")
        f.write("-" * 80 + "\n")

print("Scraping completed and saved to faculty_info.txt")
