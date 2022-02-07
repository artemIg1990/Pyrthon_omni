import logging
import config
from time import sleep
from selenium import webdriver
from common_functions import guid_generator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions

driver = webdriver.Chrome()  # Дописать параметры в конфиг, перенести сюда
                             # Переписать ексепты по-людски


def interact(method: str, element_xpath: str, value=""):
    if method == "click":
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            element.click()
        except:
            return f"ERROR: Unable to find element {element_xpath} by XPath."
    elif method == "type":
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            element.click()
            sleep(1)
            try:
                element.clear()
            except:
                print("element can't be clear")
            element.send_keys(value)
        except exceptions as ex:
            return f"ERROR: Unable to find element {element_xpath} by XPath to type {value}. Message: {ex}"
    elif method == "set":
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            if element.get_property("checked") != value:
                element.click()
        except:
            return f"ERROR: Unable to find element {element_xpath} by XPath to set status."
    elif method == "get_value":
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            try:
                value = element.get_property("value")
                return value
            except:
                value = element.text
                return value
        except:
            f"ERROR: Unable to find element {element_xpath} by XPath to get value"


def wait_for_element(driver_local, element_xpath):
    try:
        element = WebDriverWait(driver, 5).until(
            ec.presence_of_element_located((By.XPATH, element_xpath))
        )
    except:
        print(f"ERROR: Element {element} can't be found while waiting for it")
        driver_local.quit()


def log_in_cc(driver_local):
    driver_local.get(f"{config.DHurl}admin/core/order/")
    interact("type", '//*[@id="id_username"]', config.login_bh_cc)
    interact("type", '//*[@id="id_password"]', config.password_bh_cc)
    interact("click", '//*[@id="login-form"]/div[4]/input')
    wait_for_element(driver_local, '//*[@id="left-nav"]/ul/li[1]/a')

def save_changes(driver_local):
    interact("click", '//*[@id="order_form"]/div[1]/div[1]/div[1]/button[2]')
    try:
        wait_for_element(driver_local, '//*[@id="suit-center"]/div[1]')
    except:
        wait_for_element(driver_local, '//*[@id="order_form"]/div[2]/div/div')  # errors, that prevent saving
        interact("type", '//*[@id="id_client_system_id"]', "1")
        interact("type", '//*[@id="id_recipient_code"]', guid_generator())
    finally:
        interact("click", '//*[@id="order_form"]/div[1]/div[1]/div[1]/button[2]')


def cancel_order_manual(eni, driver_local):
    log_in_cc(driver_local)
    interact("type", '//*[@id="searchbar"]', eni["uid"])  # input uid to search
    interact("click", '//*[@id="changelist-search"]/div/input[2]')  # search button.  << тут нужен нормальный xPath
    wait_for_element(driver_local, '//*[@id="result_list"]')  # wait for search results
    try:
        i = 1
        while driver_local.find_element(By.XPATH, f'//*[@id="result_list"]/tbody/tr[{i}]').text.find(f"{eni['order_number']}") < 0:
            i += 1
        interact("click", f'//*[@id="result_list"]/tbody/tr[{i}]/th/a')
        wait_for_element(driver_local, '//*[@id="order_form"]')  # wait while order info loading
        status = interact("get_value", '//*[@id="id_status"]', "Отменен")
        if status != "Отменен":   # set status "Отменен"
            interact("type", '//*[@id="id_status"]', "Отменен")
            driver_local.find_element(By.XPATH, '//*[@id="id_status"]').send_keys(Keys.ENTER)   # Переписать. Выглядит некрасиво, но нет идей как сделать красиво
        interact("set", '//*[@name="is_active"]', False)   # make order non-active
        interact("click", '//*[@id="order_form"]/div[1]/div[1]/div[1]/button[2]')
        wait_for_element(driver_local, '//*[@id="suit-center"]/div[1]')  # Форма //*[@id="order_form"]/div[2]/div/div
        print("success")
    except :
        print("something went wrong")
        logging.warning(f"something went wrong: ")


eni = {"uid": "d43c40ed-f6f7-496c-84f6-f3b0c73de771", "order_number": "24710"}
orders = {"6970025875": "	e70813a6-62ff-4eaa-a4d7-53c963d20cf2", "6970281552": "2b6b2c1b-146a-457e-b2d3-dc8c4adac52a",
          "6970339465": "7f082b1f-1260-4124-8267-5b4f729950d6", "6970591896": "bdcd9460-20a1-4f50-897d-678b3de0bd35",
          "123789": "0c67b402-6f48-4163-865b-f96382c5345c", "6970467676": "35a1adfc-29ce-43a0-82bf-7d3d4c43508a",
          "6970444346": "06b36458-0b28-4928-89ab-0572f11d3bfe", "6970054116": "	40c3f5d1-2dc7-42c5-b0c1-9dcad731a954"}

for i in orders.keys():
    eni.update({"uid": orders.get(i), "order_number": i})
    cancel_order_manual(eni, driver)
