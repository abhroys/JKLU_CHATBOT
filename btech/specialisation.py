from bs4 import BeautifulSoup

# Simulated HTML content from the web pages
html_pages = {
    "b-tech-in-computer-science-engineering": """PASTE HTML OF PAGE 1""",
    "b-tech-in-computer-science-and-artificial-intelligence": """PASTE HTML OF PAGE 2""",
    "b-tech-in-computer-and-communication-engineering": """PASTE HTML OF PAGE 3"""
}

def extract_and_save(html_content, filename):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    with open(f"{filename}.txt", 'w', encoding='utf-8') as f:
        for h2 in soup.find_all('h2', class_='elementor-heading-title'):
            f.write(h2.text.strip() + "\n\n")
            p_tag = h2.find_next('p')
            if p_tag:
                f.write(p_tag.text.strip() + "\n\n")
                
        for div in soup.find_all('div', class_='bdt-accordion-item'):
            title = div.find('div', class_='bdt-title').text.strip()
            content = div.find('div', class_='bdt-accordion-content').text.strip()
            f.write(title + "\n")
            f.write(content + "\n\n")
        

for filename, html_content in html_pages.items():
    extract_and_save(html_content, filename)
