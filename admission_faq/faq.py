from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

# Initialize the Selenium WebDriver (Firefox will use GeckoDriver from PATH)
driver = webdriver.Firefox()

# URL of the page containing the FAQ (replace this with the actual URL)
faq_url = "https://jklu.edu.in/admission-faqs/"

# Directory to save the extracted text file
output_directory = "faq_info"
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Function to extract FAQ information from the page
def extract_faq_info(url):
    driver.get(url)
    time.sleep(3)  # Allow the page to load completely

    # Expand all accordion sections
    try:
        accordion_buttons = driver.find_elements(By.CLASS_NAME, 'bdt-accordion-title')
        for button in accordion_buttons:
            if button.get_attribute("aria-expanded") == "false":
                button.click()  # Expand the hidden sections
        time.sleep(1)
    except Exception as e:
        print(f"Accordion sections could not be expanded: {e}")

    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract FAQ content (questions and answers)
    faqs = ""
    faq_items = soup.find_all('div', class_='bdt-accordion-item')
    
    for faq in faq_items:
        question = faq.find('span', class_='bdt-title').get_text(strip=True)
        answer = faq.find('div', class_='bdt-accordion-content').get_text(strip=True)
        
        faqs += f"--- {question} ---\n"
        faqs += f"{answer}\n\n"

    return faqs

# Extract FAQs from the page
faq_data = extract_faq_info(faq_url)

# Create a file to save the FAQ data
file_name = "admission_faqs.txt"
file_path = os.path.join(output_directory, file_name)

# Save the extracted FAQ content to a text file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(faq_data)

print(f"FAQ data saved to {file_path}")

# Close the browser
driver.quit()

print("FAQ scraping completed.")
