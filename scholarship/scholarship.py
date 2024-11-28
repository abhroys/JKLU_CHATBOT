from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

# Initialize the Selenium WebDriver (Firefox will use GeckoDriver from PATH)
driver = webdriver.Firefox()

# List of URLs to scrape (replace these with the actual scholarship URLs)
urls = [
    "https://jklu.edu.in/b-tech-scholarships/",
"https://jklu.edu.in/bba-scholarships/",
"https://jklu.edu.in/b-des-scholarships/"
]

# Directory to save the extracted text files
output_directory = "scholarship_info"
os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Function to extract scholarship information from each page
def extract_scholarship_info(url):
    driver.get(url)
    time.sleep(3)  # Allow the page to load completely

    # Expand all accordion sections (if present)
    try:
        accordion_buttons = driver.find_elements(By.CLASS_NAME, 'bdt-accordion-title')
        for button in accordion_buttons:
            if "aria-expanded" in button.get_attribute("outerHTML") and button.get_attribute("aria-expanded") == "false":
                button.click()  # Expand the hidden sections
        time.sleep(1)
    except Exception as e:
        print(f"Accordion sections could not be expanded for {url}: {e}")
    
    # Parse the page with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Extract relevant page content, ignoring common sections like "Connect with us", "Quick Links", etc.
    content = ""

    # Extract main scholarship heading (h2, h3) and paragraphs (ignoring irrelevant sections)
    main_sections = soup.find_all(['h2', 'h3'])
    paragraphs = soup.find_all('p')

    for section in main_sections:
        section_text = section.get_text(strip=True)
        # Filter out common headings that are not part of scholarship content
        if "Connect with us" not in section_text and "Quick Links" not in section_text:
            content += f"\n--- {section_text} ---\n"
    
    for paragraph in paragraphs:
        # Again, filtering out irrelevant global content
        paragraph_text = paragraph.get_text(strip=True)
        if "JK Lakshmipat University" not in paragraph_text and "Speak to your Academic Advisor" not in paragraph_text:
            content += paragraph_text + "\n"

    # Extract all table data (scholarship breakdown)
    tables = soup.find_all('table')
    for table in tables:
        content += "\n--- Scholarship Breakdown Table ---\n"
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all(['th', 'td'])
            content += '\t'.join(col.get_text(strip=True) for col in cols) + "\n"
    
    return content

# Iterate through the list of URLs and extract information for each page
for url in urls:
    # Using the URL to identify the page type (BBA, B.Tech, B.Des) for the file name
    page_type = url.split('/')[-2] if '/' in url else "No_Title"

    scholarship_data = extract_scholarship_info(url)

    # Create a safe file name based on the page type
    file_name = page_type.replace(' ', '_').replace('/', '_') + "_scholarship.txt"
    file_path = os.path.join(output_directory, file_name)

    # Save the extracted content to a text file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(scholarship_data)

    print(f"Data for {page_type} saved to {file_path}")

# Close the browser
driver.quit()

print("Scraping completed.")
