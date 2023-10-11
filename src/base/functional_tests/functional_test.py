import time
from typing import Callable

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

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
