import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# pegando os dados de Login
login = str(input('Digite o email da sua conta do linkedin: '))
password = str(input('Digite a sua senha para fazer o login: '))

# ciração do driver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

url = 'https://www.linkedin.com/jobs/'
driver.get(url)

time.sleep(2)

# Fazendo o login no site
login_key = driver.find_element(By.ID, 'session_key')
login_key.send_keys(login)
time.sleep(1)

password_key = driver.find_element(By.ID, 'session_password')
password_key.send_keys(password)


btn_enter = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
btn_enter.click()


