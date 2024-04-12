import os
import logging
import subprocess
from typing import Iterator

import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from _pytest.fixtures import FixtureRequest

@pytest.fixture(scope='function')
# def init_browser(request: FixtureRequest) -> Iterator[WebDriver]:
def init_browser() -> Iterator[WebDriver]:
    logging.info('Init browser')
    options = Options()
    options.add_argument('--disable-extensions')
    options.add_argument('user-data-dir=data')
    options.add_argument('--start-maximized')
    path_chrome = '/home/khains@kaopiz.local/Documents/Group/group_auto_test/files/chrome-linux64/chrome'
    path_driver = '/home/khains@kaopiz.local/Documents/Group/group_auto_test/files/chromedriver-linux64/chromedriver'
    options.binary_location = path_chrome
    service = Service(executable_path=path_driver)
    driver = webdriver.Chrome(service=service, options=options)
    logging.info('Init browser: done')

    # def finalize():
    #     driver.quit()
    #
    # request.addfinalizer(finalize)
    return driver

