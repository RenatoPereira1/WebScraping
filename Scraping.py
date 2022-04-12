
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json


option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path=r'C:\Users\reap\OneDrive\Área de Trabalho\Nova_pasta\geckodriver.exe')

driver.get('https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/')



time.sleep(10)
driver.find_element_by_xpath("//div[@class='col-main']//table//thead//tr//th[@class='games']").click()
element = driver.find_element_by_xpath("//div[@class='col-main']//table")
html_content = element.get_attribute('outerHTML')



soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')



df_full = pd.read_html(str(table))[0].head(100)
df = df_full[['Times','P','J','V']]
df.columns = ['Time','Pontos', 'Jogos','Vitorias']


top10={}
top10['points'] = df.to_dict('records')
print(top10['points'])

driver.quit()

js=json.dumps(top10)
fp=open('arquivo2.json', 'w')
fp.write(js)
fp.close()