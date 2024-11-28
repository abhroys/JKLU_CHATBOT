from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

driver = webdriver.Firefox()

with open('faculty_profile_links_management.txt', 'r') as file:
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

    faculty_info = {}

    try:
        selected_publications_button = driver.find_element(By.ID, "bdt-accordion-selected-publications")
        driver.execute_script("arguments[0].scrollIntoView(true);", selected_publications_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", selected_publications_button)
        time.sleep(1)
        print(f"Successfully clicked Selected Publications accordion for {url}")
    except Exception as e:
        print(f"Error clicking Selected Publications for {url}: {e}")
        faculty_info['Selected Publications'] = "No Selected Publications information available."
        return faculty_info

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    def safe_extract(section, description):
        section_text = None
        if section:
            content = section.find_next('ul') or section.find_next('p')
            if content and content.get_text(strip=True):
                section_text = content.get_text(separator='\n', strip=True)
        return section_text if section_text else f"No {description} information available."

    education_heading = soup.find('h1', string="Education")
    if education_heading:
        education_section = education_heading.find_next('div', {'class': 'elementor-widget-container'})
        faculty_info['Education'] = safe_extract(education_section, "Education")

    experience_section = soup.find('div', {'data-id': '2ed3566'})
    if experience_section:
        experience_content = experience_section.find('p')
        if experience_content:
            faculty_info['Experience'] = experience_content.get_text(separator='\n', strip=True)
        else:
            faculty_info['Experience'] = "No Experience information available."
    else:
        faculty_info['Experience'] = "No Experience information available."

    teaching_interests_section = soup.find('div', {'data-title': 'teaching-interests'})
    if teaching_interests_section:
        teaching_interests_content = teaching_interests_section.find_next('ul')
        if teaching_interests_content:
            faculty_info['Teaching Interests'] = teaching_interests_content.get_text(separator='\n', strip=True)
        else:
            faculty_info['Teaching Interests'] = "No Teaching Interests information available."
    else:
        faculty_info['Teaching Interests'] = "No Teaching Interests information available."

    research_interests_section = soup.find('div', {'data-title': 'research-interests'})
    faculty_info['Research Interests'] = safe_extract(research_interests_section, "Research Interests")

    honors_awards_section = soup.find('div', {'data-title': 'honours-awards-and-affiliations'})
    faculty_info['Honors, Awards, and Affiliations'] = safe_extract(honors_awards_section, "Honors, Awards, and Affiliations")

    selected_publications_section = soup.find('div', {'id': 'bdt-accordion-selected-publications'})
    if selected_publications_section:
        publications_list = selected_publications_section.find('ul')
        if publications_list:
            faculty_info['Selected Publications'] = publications_list.get_text(separator='\n', strip=True)
        else:
            print(f"No publications found under Selected Publications for {url}")
            faculty_info['Selected Publications'] = "No Selected Publications information available."
    else:
        print(f"No Selected Publications section found for {url}")
        faculty_info['Selected Publications'] = "No Selected Publications information available."

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
