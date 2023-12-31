import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = 'https://mzsp.pl'

driver.get(url)
soup = BeautifulSoup(driver.page_source, features='lxml')

headings = soup.find_all(name='div', attrs={'class': 'container'})
for heading in headings:
    print(heading.getText())

time.sleep(10)

driver.quit()