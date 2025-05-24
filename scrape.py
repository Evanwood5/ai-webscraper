from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def scrape_website(website):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(website)
        html = driver.page_source
        return html
    finally:
        driver.quit()


#code that will help clean html content
from bs4 import BeautifulSoup

def extract_body_content(html_content):
	soup = BeautifulSoup(html_content, "html.parser")
	body_content = soup.body
	if body_content:
		return str(body_content)
	return""

def clean_body_content(body_content):
	soup =BeautifulSoup(body_content, "html.parser")
	
	#getting rid of style and script tags (not needed)
	for script_or_style in soup(["script","style"]):
		script_or_style.extract()
	
	#get all text and separate with new line
	cleaned_content = soup.get_text(separator="\n")
	#remove any back slash n characters that are unessesary
	cleaned_content = "\n".join(
		line.strip() for line in cleaned_content.splitlines() if line.strip()
	)
	
	return cleaned_content

#can only bring in so much contnent
def split_dom_content(dom_content,max_length=6000):
	return[
	dom_content[i: i + max_length] for i in range(0,len(dom_content),max_length)
	]

