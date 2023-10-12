from base.functional_tests.functional_test import FunctionalTest

from django.urls import reverse

from selenium.webdriver.common.by import By


class NavbarTest(FunctionalTest):
    def test_navbar_item_of_home_redirects_to_home_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.NAME, 'home').click()

        self.wait_for(lambda: self.assertEqual(self.browser.current_url, self.live_server_url + reverse('home')))

    def test_navbar_brand_redirects_to_home_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.NAME, 'brand').click()

        self.wait_for(lambda: self.assertEqual(self.browser.current_url, self.live_server_url + reverse('home')))

    def test_navbar_item_of_product_list_redirects_to_product_list_page(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.NAME, 'product_list').click()

        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, self.live_server_url + reverse('products:list'))
        )
