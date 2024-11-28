from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

driver = webdriver.Firefox()

base_url = "https://www.jklu.edu.in"

all_links = set()

excluded_domains = ['linkedin.com', 'twitter.com', 'youtube.com', 'facebook.com', 'instagram.com']
excluded_file_types = ['.jpeg', '.jpg', '.png', '.svg', '.gif']

def scrape_links_from_page(url):
    driver.get(url)
    time.sleep(3)

    page_links = set()
    retry_count = 0
    max_retries = 3
    
    while retry_count < max_retries:
        try:
            elements = driver.find_elements(By.TAG_NAME, 'a')
            for element in elements:
                href = element.get_attribute('href')
                if href:
                    if href.startswith('/'):
                        href = base_url + href

                    if not any(domain in href for domain in excluded_domains) and not any(href.endswith(ext) for ext in excluded_file_types):
                        page_links.add(href)
            break
        except StaleElementReferenceException:
            retry_count += 1
            print(f"Encountered a stale element, retrying... ({retry_count}/{max_retries})")
            time.sleep(1)
    
    return page_links

def handle_pagination():
    try:
        next_button = driver.find_element(By.CLASS_NAME, 'next.page-numbers')
        if next_button:
            next_button.click()
            time.sleep(3)
            return True
    except NoSuchElementException:
        return False

def recursive_scrape(url, visited_pages):
    if url in visited_pages:
        return

    print(f"Visiting: {url}")
    visited_pages.add(url)
    new_links = scrape_links_from_page(url)
    all_links.update(new_links)

    while handle_pagination():
        new_paginated_links = scrape_links_from_page(driver.current_url)
        all_links.update(new_paginated_links)

    for link in new_links:
        if link.startswith(base_url) and link not in visited_pages:
            recursive_scrape(link, visited_pages)

visited_pages = set()
recursive_scrape(base_url, visited_pages)

driver.quit()

output_file_path = 'all_collected_jklu_links_firefox.txt'
with open(output_file_path, 'w') as file:
    for link in all_links:
        file.write(f"{link}\n")

print(f"Total links found: {len(all_links)}")
