from base.functional_tests.functional_test import FunctionalTest

from django.urls import reverse


class NavbarTest(FunctionalTest):
    def test_navbar_item_of_home_redirects_to_home_page(self):
        self.browser.get(self.live_server_url)
        self.go_to_page_by_navbar('home', reverse('home'))

    def test_navbar_brand_redirects_to_home_page(self):
        self.browser.get(self.live_server_url)
        self.go_to_page_by_navbar('brand', reverse('home'))

    def test_navbar_item_of_product_list_redirects_to_product_list_page(self):
        self.browser.get(self.live_server_url)
        self.go_to_page_by_navbar('product_list', reverse('products:list'))

    def test_navbar_item_of_cart_redirects_to_cart_page(self):
        self.browser.get(self.live_server_url)
        self.go_to_page_by_navbar('cart', reverse('carts:cart'))
