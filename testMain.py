from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#selenium configura el driver automaticamente
driver = webdriver.Chrome()

#abre pagina web
driver.get("https://www.google.comfrd")
time.sleep(5)

#print("Selenium funciona correctamente")

#cierra navegador
driver.quit()
