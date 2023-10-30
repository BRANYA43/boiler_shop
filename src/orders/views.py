from carts.cart import Cart

from django.urls import reverse_lazy
from django.views.generic import FormView


from orders.forms import CustomerForm
from orders.models import Customer, Order, OrderProduct


class MakeOrderView(FormView):
    form_class = CustomerForm
    template_name = 'orders/make_order.html'
    success_url = reverse_lazy('orders:success_making_order')

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
        self.cart.clear()
        return super().form_valid(form)

    def _set_customer(self, customer: Customer):
        self.cart.customer = customer

    def _create_order_products(self, order):
        for product, quantity in self.cart:
            OrderProduct.objects.create(
                order=order,
                product=product,
                name=product.name,
                price=product.price,
                quantity=quantity,
            )
