from carts.cart import Cart

from django.http import HttpRequest
from django.shortcuts import redirect, render

from orders.forms import CustomerForm
from orders.models import Customer, Order, OrderProduct

from products.models import Product


def make_order_view(request: HttpRequest):
    cart = Cart(request)
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'orders/make_order.html', {'form': form, 'cart': cart})
    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            _form_is_valid(request, cart, form)
            return redirect('orders:make_order_success_message')
        else:
            return render(request, 'orders/make_order.html', {'form': form, 'cart': cart})


def _form_is_valid(request: HttpRequest, cart: Cart, form: CustomerForm):
    customer = form.save()
    _set_session_customer_pk(request, customer)
    order = Order.objects.create(customer=customer)
    _create_order_products(order, cart)


def _create_order_products(order: Order, cart: Cart):
    for slug, data in cart.cart.items():
        product = Product.objects.get(slug=slug)
        OrderProduct.objects.create(
            order=order, product=product, name=data['name'], price=data['price'], quantity=data['quantity']
        )


def _set_session_customer_pk(request: HttpRequest, customer: Customer):
    session = request.session
    session['customer_id'] = customer.pk
    session.modified = True
