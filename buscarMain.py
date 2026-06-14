from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
opciones = Options()
opciones.add_argument("--disable-blink-features=AutomationControlled")
opciones.add_experimental_option("excludeSwitches", ["enable-automation"])
opciones.add_experimental_option('useAutomationExtension', False)
opciones.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

#selenium configura el driver automaticamente
driver = webdriver.Chrome(options=opciones)
try: 
    driver.get("https://www.google.com")
    time.sleep(10)
    caja_busqueda = driver.find_element(By.NAME, "q")
    caja_busqueda.send_keys("Helloween band")
    caja_busqueda.send_keys(Keys.ENTER)

    print("Busqueda realizada con exito")
    time.sleep(10)
except Exception as e:
    print(f"Ocurrió un error: {e}")
finally:
    driver.quit()
