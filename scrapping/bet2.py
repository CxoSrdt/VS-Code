from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

driver = webdriver.Firefox()

driver.get("https://www.bet365.com/#/HO/")


#tab_ev = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[7]/div[3]/span")
