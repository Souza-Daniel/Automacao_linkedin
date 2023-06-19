import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys


# mostrando as possibilidades de vagas para se pesquisar

print('1 - Analista de Dados\n2 - Eng. de Dados\n3 - Cientista de Dados')

while True:
    vaga = int(input('Digite o numero para buscar a sua vaga ideal: '))
    if vaga == 1:
        busc_vaga = 'Analista%20de%20Dados'
        break
    elif vaga == 2:
        busc_vaga = 'Engenharia%20de%20Dados'
        break
    elif vaga == 3:
        busc_vaga = 'Cientista%20de%20Dados'
        break
    else:
        print('Não encontramos este tipo de vagas em nosso histórico')

# ciração do driver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

url = f'https://www.linkedin.com/jobs/search?keywords={busc_vaga}&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
driver.get(url)
time.sleep(2)

num_vagas = driver.find_element(By.XPATH, '//*[@id="main-content"]/div')
num_vagas = num_vagas.text.split()[0].replace('.', '')
num_vagas = int(num_vagas)


while True:
    time.sleep(2)
    vagas = driver.find_element(By.ID, 'main-content').find_elements(By.TAG_NAME, 'li')
    print(len(vagas))
    if len(vagas) != 1000:
        try:
            driver.find_element(By.XPATH, '//*[@id="main-content"]/section[2]/button').click()

        except selenium.common.exceptions.ElementNotInteractableException:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    else:
        break


time.sleep(2)
num_vagas = driver.find_element(By.XPATH, '//*[@id="main-content"]/div')
print(num_vagas.text.split()[0])
vagas = driver.find_element(By.ID, 'main-content').find_elements(By.TAG_NAME, 'li')
print(len(vagas))
lista_vagas = []
cont = 0
for i in vagas:
    if 'Analista De Dados' in i.text.split('\n')[0].title():
        vaga = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
        lista_vagas.append(vaga)

print(lista_vagas)

print(f'O número de vagas disponiveis é {cont}')

for n in lista_vagas:
    driver.get(n)
    descricao_vaga = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/section[1]/div/div/section/div')
    print(f'Descrição vaga {descricao_vaga.text}')
    time.sleep(10)

driver.close()

# https://br.linkedin.com/jobs/view/analista-de-dados-bi-jr-at-m%C3%A9todo-engenharia-3608539899?refId=HFV6laE1qMSCKhYIZK7bjQ%3D%3D&trackingId=St9OvScgrKMbdYMXAjQAPg%3D%3D&position=4&pageNum=0&trk=public_jobs_jserp-result_search-card
# https://www.linkedin.com/jobs/search?keywords=Analista%20de%20Dados&location=Brasil&geoId=106057199&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0#main-content
