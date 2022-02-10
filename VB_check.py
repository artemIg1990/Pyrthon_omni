import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium_assist_methods
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions


driver_options = Options()
driver_options.add_argument(f"--window-size={config.window_size}")  # вынести
devise_em = {"deviceName": "iPad Pro"}
driver_options.add_experimental_option("mobileEmulation", devise_em)
driver_vb = webdriver.Chrome(options=driver_options)
driver_vb.get(config.VB_url)


def non_parcelok():
    element_main = driver_vb.find_element(By.XPATH, '//*[@id="root"]')
    selenium_assist_methods.interact("click", '//*[@text="ОТПРАВИТЬ ПОСЫЛКУ"]')
    selenium_assist_methods.wait_for_element(driver_vb, '')



sleep(1)
non_parcelok()
