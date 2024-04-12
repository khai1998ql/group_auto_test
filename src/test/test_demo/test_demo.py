import time
import logging

import pyautogui
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from src.main.UltilPackage.helpers import Helpers
from src.main.UltilPackage.conftest import init_browser

def test_open_broweser(init_browser: WebDriver) -> None:

    time.sleep(10)

def test_open_menu_setting(init_browser: WebDriver) -> None:
    print('Open menu setting')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f')
    time.sleep(5)

def test_switch_tab(init_browser: WebDriver) -> None:
    print('Switch tab')
    driver = init_browser
    time.sleep(2)
    driver.get('http://example.com/')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://vnexpress.vn/')
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

def test_count_tab(init_browser: WebDriver) -> None:
    print('Count tab')
    driver = init_browser
    time.sleep(2)
    driver.get('http://example.com/')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.get('http://vnexpress.vn/')
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
    count = len(driver.window_handles)
    print('Count tab', count)

def test_move_mouse(init_browser: WebDriver) -> None:
    print('Move mouse')
    time.sleep(1)
    pyautogui.moveTo(100, 100)
    time.sleep(2)
    pyautogui.moveTo(200, 200)
    time.sleep(2)
    pyautogui.moveTo(300, 300)

def test_open_url(init_browser: WebDriver) -> None:
    print('Open url')
    driver = init_browser
    driver.get('http://example.com/')
    time.sleep(2)

def test_get_title(init_browser: WebDriver) -> None:
    print('Get title')
    driver = init_browser
    driver.get('http://example.com/')
    time.sleep(2)
    title = driver.title
    print('title: ', title)

def test_find_element(init_browser: WebDriver) -> None:
    print('Open url')
    driver = init_browser
    driver.get('http://example.com/')
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//a')
    text = element.text
    print('text: ', text)

def test_click_element(init_browser: WebDriver) -> None:
    print('Open url')
    driver = init_browser
    driver.get('http://example.com/')
    time.sleep(2)
    element = driver.find_element(By.XPATH, '//a')
    ActionChains(driver).move_to_element(element).click().perform()
    time.sleep(2)


