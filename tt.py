import logging
import requests
import config
import random
import string
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
Переписать поиск элеметов по xPath по-людски, чтоб тест не валился при изменении верстки
'''
driver = webdriver.Chrome()


def cancel_order_manual(driver, eni):
    driver.get(f"{config.DHurl}admin/")
    login = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    login.click()
    login.send_keys(config.login_bh_cc)
    password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    password.click()
    password.send_keys(config.password_bh_cc)
    driver.find_element(By.XPATH, '//*[@id="login-form"]/div[4]/input').click()

    wait_for_element(driver, '//*[@id="left-nav"]/ul/li[1]/a')

    driver.get(f"{config.DHurl}admin/core/order/")

    # это тоже переписать ожиданием
    sleep(3)

    keywords = driver.find_element(By.XPATH, '//*[@id="searchbar"]')
    keywords.click()
    keywords.send_keys(eni["uid"])
    search = driver.find_element(By.XPATH, '//*[@id="changelist-search"]/div/input[2]')   # << тут нужен нормальный xPath
    search.click()
    sleep(1)   # << заменить ожиданием
    try:
        i = 1
        while driver.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{i}]').text.find(f"{eni['order_number']}") < 0:
            i += 1
        order_open = driver.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{i}]/th/a')
        sleep(1)
        order_open.click()
        status_bar = driver.find_element(By.XPATH, '//*[@id="id_status"]')
        if status_bar.text != "Отменен":
            status_bar.click()
            status_bar.send_keys("Отменен")
            status_bar.send_keys(Keys.ENTER)
        is_active_checkbox = driver.find_element(By.XPATH, '//*[@name="is_active"]')
        if is_active_checkbox.get_property("checked"):
            is_active_checkbox.click()
        save_btn = driver.find_element(By.XPATH, '//*[@id="order_form"]/div[1]/div[1]/div[1]/button[2]')
        save_btn.click()
        sleep(3)    # Заменить ожиданием элемента '//*[@id="suit-center"]/div[1]'
        print("1")
    except:
        print("something went wrong")
        logging.warning(f"something went wrong: ")

    finally:
        driver.close()


def wait_for_element(driver_local, element_xpath):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, element_xpath))
        )
    except:
        print(f"ERROR: Element {element} can't be found while waiting for it")
        driver_local.quit()


def interact_element(driver, element, text="", is_checked = True):
    if element is True:
        print("1")


cancel_order_manual({"uid": "17f7d9b6-b77b-41d6-9645-025af67cef76", "order_number": "[CDK]1307784852"})

"""
di = {"24709":"4a444827-35a1-4c68-83a8-faf5c6cc1c32", "24710": "d43c40ed-f6f7-496c-84f6-f3b0c73de771", "24711": "568c5cbe-3230-40ee-8c99-5962bbb57822"}

for i in di.keys():
    cancel_order_manual({"uid": di.get(i), "order_number": i})
    print(di.get(i), i)
"""
