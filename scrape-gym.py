import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
chrome_driver_manager = ChromeDriverManager(log_level=logging.CRITICAL).install()
service = Service(chrome_driver_manager)
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://smartentry.org/queue/book/e1tpy")

XPATH = "/html/body/div[4]/div[1]/div/div[2]"
queue = driver.find_element(by=By.XPATH, value=XPATH)

print(queue.text)
