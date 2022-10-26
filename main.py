from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn = browser.find_element(By.ID, 'book')
    btn.click()

    el_x = browser.find_element(By.ID, 'input_value').text

    st = browser.find_element(By.ID, 'answer')
    st.send_keys(calc(el_x))

    btn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    btn.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    browser.quit()
