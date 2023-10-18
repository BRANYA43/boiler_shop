from django.urls import reverse

from products.tests.test_model import create_test_product

from selenium.webdriver.common.by import By

from .functional_test import FunctionalTest


class ProductListPageTest(FunctionalTest):
    def test_product_name_redirects_user_to_product_detail(self):
        product = create_test_product()

        self.browser.get(self.live_server_url + reverse('products:list'))
        card = self.browser.find_element(By.CSS_SELECTOR, '.card')
        card.find_element(By.NAME, 'name_link').click()

        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, self.live_server_url + product.get_absolute_url())
        )

    def test_product_image_redirects_user_to_product_detail(self):
        product = create_test_product()

        self.browser.get(self.live_server_url + reverse('products:list'))
        card = self.browser.find_element(By.CSS_SELECTOR, '.card')
        card.find_element(By.NAME, 'image_link').click()

        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, self.live_server_url + product.get_absolute_url())
        )
