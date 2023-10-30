import time
from typing import Callable

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from webdriver_manager import firefox

firefox.GeckoDriverManager().install()

MAX_WAIT = 10


def wait(fn: Callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (WebDriverException, AssertionError) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    return wrapper


class FunctionalTest(StaticLiveServerTestCase):
    @staticmethod
    def get_browser():
        return webdriver.Firefox()

    def setUp(self) -> None:
        self.browser = self.get_browser()

    def tearDown(self) -> None:
        self.browser.quit()

    @wait
    def wait_for(self, fn: Callable):
        return fn()

    @wait
    def wait_for_check_current_url(self, expected_url):
        self.assertEqual(self.browser.current_url, self.live_server_url + expected_url)

    def go_to_page_by_navbar(self, name_page: str, url_for_check: str):
        navbar = self.browser.find_element(By.TAG_NAME, 'nav')
        navbar.find_element(By.NAME, name_page).click()
        self.wait_for_check_current_url(url_for_check)
