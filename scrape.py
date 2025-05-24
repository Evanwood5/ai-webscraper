
import selenium.webdriver as webdriver 
from selenium.webdriver.chrome.service import Service

def scrape_website(website):
	print("Launching chrome browser")

	#allows for us to control chrome thorugh application (chrome driver)
	chrome_driver_path = "./chromedriver.exe"
	# specify how the webdriver should operate
	options = webdriver.ChromeOptions()
	#specify service we are using (where ever chrom application lives)
	driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options)

	try:
		driver.get(website)
		print("page loaded...")
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

