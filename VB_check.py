import config
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from common_functions import guid_generator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions


driver_options = Options()
driver_options.add_argument(f"--window-size={config.window_sise}")  # вынести
driver = webdriver.Chrome(options=driver_options)


driver.get(config.VB_url)
sleep(1)
