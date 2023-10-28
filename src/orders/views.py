from carts.cart import Cart

from django.urls import reverse_lazy
from django.views.generic import FormView


from orders.forms import CustomerForm
from orders.models import Customer, Order, OrderProduct

from products.models import Product


class MakeOrderView(FormView):
    form_class = CustomerForm
    template_name = 'orders/make_order.html'
    success_url = reverse_lazy('orders:make_order_success_message')

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.cart = Cart(self.request)

    def get_context_data(self, **kwargs):
        self.extra_context = {'cart': self.cart}
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        customer = form.save()
        self._set_customer(customer)
        order = Order.objects.create(customer=customer)
        self._create_order_products(order)
        return super().form_valid(form)

    def _set_customer(self, customer: Customer):
        session = self.request.session
        session['customer'] = customer.pk
        session.save()

    def _create_order_products(self, order):
        for slug, data in self.cart.cart.items():
            product = Product.objects.get(slug=slug)
            OrderProduct.objects.create(order=order, product=product, **data)
