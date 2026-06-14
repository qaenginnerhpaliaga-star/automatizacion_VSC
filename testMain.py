from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#selenium configura el driver automaticamente
driver = webdriver.Chrome()

#abre pagina web
driver.get("https://www.google.com")
time.sleep(15)

print("Selenium funciona correctamente")

#cierra navegador
driver.quit()
