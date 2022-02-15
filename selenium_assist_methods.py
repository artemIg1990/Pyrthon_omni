import logging
import config
from time import sleep
from selenium import webdriver
from  selenium.webdriver.remote.command import Command
from common_functions import guid_generator
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions

# driver = webdriver.Chrome()  # Дописать параметры в конфиг, перенести сюда
                             # Переписать ексепты по-людски


def interact(driver, method: str, element_xpath: str, value=""):
    if method == "click":
        try:
            element = driver.find_element(By.XPATH, element_xpath)
            element.click()
        except exceptions as ex:
            return f"ERROR: Unable to find element {element_xpath} by XPath., {ex}"
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
        if driver.find_element(By.XPATH, '//*[@id="id_client_system_id"]').text == "":
            interact("type", '//*[@id="id_client_system_id"]', "1")
        interact("click", '//*[@id="order_form"]/div[1]/div[1]/div[1]/button[2]')
        wait_for_element(driver_local, '//*[@id="suit-center"]/div[1]')  # Форма //*[@id="order_form"]/div[2]/div/div
        print("success")
    except :
        print("something went wrong")
        logging.warning(f"something went wrong: ")


eni = {"uid": "d43c40ed-f6f7-496c-84f6-f3b0c73de771", "order_number": "24710"}
orders = {"6970544844": "d40e4e23-ed00-4f89-8fe3-53103cbf7363"}
"""
for i in orders.keys():
    eni.update({"uid": orders.get(i), "order_number": i})
    cancel_order_manual(eni, driver)
"""

class TouchActions(object):
    """
    Generate touch actions. Works like ActionChains; actions are stored in the
    TouchActions object and are fired with perform().
    """

    def __init__(self, driver):
        """
        Creates a new TouchActions object.
        Args:
            -driver: The WebDriver instance, which must be touchscreen enabled.
        """
        self._driver = driver
        self._actions = []

    def perform(self):
        """
        Performs all stored actions.
        """
        for action in self._actions:
            action()

    def tap(self, on_element):
        """
        Taps on a given element.
        Args:
            -element: The element to tap.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.SINGLE_TAP, {'element': on_element.id}))
        return self

    def double_tap(self, on_element):
        """
        Double taps on a given element.
        Args:
            -element: The element to tap.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.DOUBLE_TAP, {'element': on_element.id}))
        return self

    def tap_and_hold(self, xcoord, ycoord):
        """
        Tap and hold a given element.
        Args:
            -xcoord: X Coordinates.
            -ycoord: Y Coordinates.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.TOUCH_DOWN, {
                'x': xcoord,
                'y': ycoord}))
        return self

    def move(self, xcoord, ycoord):
        """
        Move held tap to specified location.
        Args:
            -xcoord: X Coordinates.
            -ycoord: Y Coordinates.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.TOUCH_MOVE, {
                'x': xcoord,
                'y': ycoord}))
        return self

    def release(self, xcoord, ycoord):
        """
        Release previously issued tap and hold command, at specified location.
        Args:
            -xcoord: X Coordinates.
            -ycoord: Y Coordinates.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.TOUCH_UP, {
                'x': xcoord,
                'y': ycoord}))
        return self

    def scroll(self, xoffset, yoffset):
        """
        Touch and scroll, moving by xoffset and yoffset.
        Args:
            -xoffset: X offset to move to.
            -yoffset: Y offset to move to.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.TOUCH_SCROLL, {
                'xoffset': xoffset,
                'yoffset': yoffset}))
        return self

    def scroll_from_element(self, on_element, xoffset, yoffset):
        """
        Touch and scroll starting at on_element, moving by xoffset and yoffset.
        Args:
            -on_element: Element where scroll starts.
            -xoffset: X offset to move to.
            -yoffset: Y offset to move to.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.TOUCH_SCROLL, {
                'element': on_element.id,
                'xoffset': xoffset,
                'yoffset': yoffset}))
        return self

    def long_press(self, on_element):
        """
        Long press on an element.
        Args:
            -on_element: The element to long press.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.LONG_PRESS, {'element': on_element.id}))
        return self

    def flick(self, xspeed, yspeed):
        """
        Flicks, starting anywhere on the screen.
        Args:
            -xspeed: The X speed in pixels per second.
            -yspeed: The Y speed in pixels per second.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.FLICK, {
                'xSpeed': xspeed,
                'ySpeed': yspeed}))
        return self

    def flick_element(self, on_element, xoffset, yoffset, speed):
        """
        Flick starting at on_element, and moving by the xoffset and yoffset.
        Args:
            -on_element: Flick will start at center of element.
            -xoffset: X offset to flick to.
            -yoffset: Y offset to flick to.
            -speed: Pixels per second to flick.
        """
        self._actions.append(lambda:
            self._driver.execute(Command.FLICK, {
                'element': on_element.id,
                'xoffset': xoffset,
                'yoffset': yoffset,
                'speed': speed}))
        return self
