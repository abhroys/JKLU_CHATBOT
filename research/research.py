from selenium import webdriver
from bs4 import BeautifulSoup
import time

# Initialize the Selenium WebDriver (make sure geckodriver is in your PATH or specify its location)
driver = webdriver.Firefox()

# Open the webpage
url = "https://jklu.edu.in/research/"  # replace with the actual URL
driver.get(url)

# Wait for the page to load (you can use WebDriverWait for specific conditions)
time.sleep(5)

# Get the page source
html = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(html, 'html.parser')

# Open a text file to write the extracted text in a well-formatted manner
with open('extracted_text_for_chatbot.txt', 'w', encoding='utf-8') as file:

    # Extract accordion titles and save them with proper formatting
    accordion_titles = soup.find_all('div', class_='bdt-accordion-title')
    file.write("### Accordion Titles ###\n")
    for title in accordion_titles:
        formatted_title = f"- {title.get_text(strip=True)}\n"
        file.write(formatted_title)

    file.write("\n----------------------\n\n")

    # Extract carousel contents and format them
    carousel_items = soup.find_all('div', class_='uc_classic_carousel_content')
    file.write("### Carousel Items ###\n")
    for idx, item in enumerate(carousel_items, 1):
        formatted_item = f"{idx}. {item.get_text(strip=True)}\n"
        file.write(formatted_item)

    file.write("\n----------------------\n\n")

    # Extract accordion content (hidden sections) and format the text
    accordion_contents = soup.find_all('div', class_='bdt-accordion-content')
    file.write("### Accordion Content ###\n")
    for idx, content in enumerate(accordion_contents, 1):
        if content.text:
            formatted_content = f"Section {idx}:\n{content.get_text(strip=True)}\n"
            file.write(formatted_content)
            file.write("\n----------------------\n\n")

# Close the browser driver
driver.quit()
