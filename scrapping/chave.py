from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
#from anticaptchaofficial.recaptchav2proxyless import *
import time

nav = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
link = "https://www.milionariotips.com.br"
nav.get(link)

chave_captcha = nav.find_element(By.XPATH('/html/body/script[15]')).get_attribute('sitekey')

#solver = recaptchaV2ProxyLess()
#solver.set_verbose(1)
#solver.set_key("9b89a274d48cb015dcf4a4d78477b569")
#solver.set_website_url(link)
#solver.set_website_key(chave_captcha)
#resposta = solver.solve_and_return_solution()
#if resposta != 0:
#    print(resposta)
#else:
#    print(solver.err_string)
#time.sleep(100)