from time import sleep as zz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

url = 'https://www.youtube.com/'
driver.get(url)
driver.find_element(By.TAG_NAME, 'input').send_keys('ghost')
driver.find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)
zz(1)
driver.find_element(By.LINK_TEXT, 'Ghost - Square Hammer (Official Music Video)').click()
zz(10)

