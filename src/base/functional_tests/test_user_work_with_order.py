from base.functional_tests.functional_test import FunctionalTest

from django.urls import reverse

from products.tests.test_model import create_test_product

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class UserWorkWithOrderTest(FunctionalTest):
    def test_user_can_order_product_form_product_list(self):
        product = create_test_product()

        # Use enters to site
        self.browser.get(self.live_server_url)

        # User goes to products page
        self.go_to_page_by_navbar('product_list', reverse('products:list'))

        # User chooses product and click on Buy
        self.buy_product_through_product_list()

        # User goes to cart to check if chosen product is there
        self.go_to_page_by_navbar('cart', reverse('carts:cart'))
        cart_product_list = self.browser.find_element(By.ID, 'id_product_list').text
        self.assertIn(product.name, cart_product_list)

        # User click on Make Order
        self.browser.find_element(By.NAME, 'make_order').click()
        self.wait_for_check_current_url(reverse('orders:make_order'))

        # User fill customer form
        first_name = self.browser.find_element(By.NAME, 'first_name')
        first_name.send_keys('First name')
        first_name.send_keys(Keys.ENTER)

        last_name = self.browser.find_element(By.NAME, 'last_name')
        last_name.send_keys('Last name')
        last_name.send_keys(Keys.ENTER)

        phone = self.browser.find_element(By.NAME, 'phone')
        phone.send_keys('+380505555555')
        phone.send_keys(Keys.ENTER)

        # User click finish order
        self.browser.find_element(By.NAME, 'finish_order').click()

        # Site show message about success making order
        self.wait_for_check_current_url(reverse('orders:success_making_order'))

    def test_user_can_order_product_from_product_detail(self):
        product = create_test_product()

        # Use enters to site
        self.browser.get(self.live_server_url)

        # User goes to products page
        self.go_to_page_by_navbar('product_list', reverse('products:list'))

        # User chooses product and click on its name for see its detail
        product_list = self.browser.find_element(By.ID, 'id_product_list')
        card = product_list.find_element(By.CLASS_NAME, 'card')
        card.find_element(By.LINK_TEXT, product.name).click()

        # User click on Buy
        self.wait_for_check_current_url(product.get_absolute_url())
        self.browser.find_element(By.NAME, 'buy').click()
        # # Button change its name to Added to cart
        self.wait_for_check_current_url(product.get_absolute_url())
        self.browser.find_element(By.NAME, 'added_to_cart')

        # User goes to cart to check if chosen product is there
        self.go_to_page_by_navbar('cart', reverse('carts:cart'))
        cart_product_list = self.browser.find_element(By.ID, 'id_product_list').text
        self.assertIn(product.name, cart_product_list)

        # User click on Make Order
        self.browser.find_element(By.NAME, 'make_order').click()
        self.wait_for_check_current_url(reverse('orders:make_order'))

        # User fill customer form
        first_name = self.browser.find_element(By.NAME, 'first_name')
        first_name.send_keys('First name')
        first_name.send_keys(Keys.ENTER)

        last_name = self.browser.find_element(By.NAME, 'last_name')
        last_name.send_keys('Last name')
        last_name.send_keys(Keys.ENTER)

        phone = self.browser.find_element(By.NAME, 'phone')
        phone.send_keys('+380505555555')
        phone.send_keys(Keys.ENTER)

        # User click finish order
        self.browser.find_element(By.NAME, 'finish_order').click()

        # Site show message about success making order
        self.wait_for_check_current_url(reverse('orders:success_making_order'))
