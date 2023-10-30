from base.functional_tests.functional_test import FunctionalTest

from django.urls import reverse

from products.tests.test_model import create_test_product

from selenium.webdriver.common.by import By


class TestUserWorkWithCart(FunctionalTest):
    def test_user_can_add_product_to_cart_from_product_list(self):
        product = create_test_product()

        # Use enters to site
        self.browser.get(self.live_server_url)

        # User goes to products page
        self.go_to_page_by_navbar('product_list', reverse('products:list'))

        # User chooses product and click on Buy
        product_list = self.browser.find_element(By.ID, 'id_product_list')
        card = product_list.find_element(By.CLASS_NAME, 'card')
        card.find_element(By.NAME, 'buy').click()
        # # Button change its name to Added to cart
        self.wait_for_check_current_url(reverse('products:list'))
        product_list = self.browser.find_element(By.ID, 'id_product_list')
        card = product_list.find_element(By.CLASS_NAME, 'card')
        card.find_element(By.NAME, 'added_to_cart')

        # User goes to cart to check if chosen product is there
        self.go_to_page_by_navbar('cart', reverse('carts:cart'))
        cart_product_list = self.browser.find_element(By.ID, 'id_product_list').text
        self.assertIn(product.name, cart_product_list)

    def test_user_can_add_product_to_cart_from_product_detail(self):
        product = create_test_product()

        # User enters to site
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

    def test_user_can_remove_product_from_cart(self):
        product = create_test_product()

        # User enters to site
        self.browser.get(self.live_server_url)

        # User goes to products page
        self.go_to_page_by_navbar('product_list', reverse('products:list'))

        # User chooses product and click on Buy
        product_list = self.browser.find_element(By.ID, 'id_product_list')
        card = product_list.find_element(By.CLASS_NAME, 'card')
        card.find_element(By.NAME, 'buy').click()

        # User goes to cart to remove product from cart
        self.go_to_page_by_navbar('cart', reverse('carts:cart'))
        cart_product_list = self.browser.find_element(By.ID, 'id_product_list')
        self.assertIn(product.name, cart_product_list.text)
        cart_product_list.find_element(By.NAME, 'remove').click()

        # User check product is removed
        self.wait_for_check_current_url(reverse('carts:cart'))
        cart_product_list = self.browser.find_element(By.ID, 'id_product_list')
        self.assertNotIn(product.name, cart_product_list.text)
