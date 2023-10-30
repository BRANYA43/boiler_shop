from base.functional_tests.functional_test import FunctionalTest

from django.urls import reverse

from products.tests.test_model import create_test_product

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class OrdersAndCartTest(FunctionalTest):
    def test_user_can_order_a_product_form_products_list(self):
        product = create_test_product()

        # User go to product list page
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.NAME, 'product_list').click()
        self.wait_for_check_current_url(reverse('products:list'))

        # User choose product to buy and click on button "Buy", product is added to cart.
        card = self.browser.find_element(By.CSS_SELECTOR, '.card')
        card.find_element(By.NAME, 'buy').click()

        # - Button change its name on "Added to cart"
        self.wait_for(lambda: self.browser.find_element(By.NAME, 'added_to_cart'))

        # User want to check his cart and see his product that have been added recently
        self.browser.find_element(By.NAME, 'cart').click()
        self.wait_for_check_current_url(reverse('carts:cart'))
        self.assertIn(product.name, self.browser.find_element(By.TAG_NAME, 'h3').text)

        # User want to continue order, so click on button "Make the Order"
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

    def test_user_can_order_a_product_form_product_detail(self):
        product = create_test_product()

        # User go to detail of chosen product
        self.browser.get(self.live_server_url + product.get_absolute_url())
        self.wait_for_check_current_url(product.get_absolute_url())

        # User click on Buy
        self.browser.find_element(By.NAME, 'buy').click()
        # - Button change name to Added to cart
        self.wait_for(lambda: self.browser.find_element(By.NAME, 'added_to_cart'))

        # User go to cart
        self.browser.find_element(By.NAME, 'cart').click()
        self.wait_for_check_current_url(reverse('carts:cart'))

        # User check what his chosen product is here
        self.assertIn(product.name, self.browser.find_element(By.TAG_NAME, 'h3').text)

        # User click on make order and go to make order page
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

        # User click on finish order
        self.browser.find_element(By.NAME, 'finish_order').click()

        # Site show message about success making order
        self.wait_for_check_current_url(reverse('orders:success_making_order'))
