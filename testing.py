import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

server_url = sys.argv[1]

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
driver.get(server_url)
assert 'Welcome to the PHP app running in a Docker container!' in driver.page_source
driver.quit()
