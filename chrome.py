from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--lang=fr')
driver = webdriver.Chrome("/home/spathare/python-practise/chromedriver",chrome_options=options)
driver.get("https://www.ansible.com/tower-trial")
sleep(3000)
driver.quit()
