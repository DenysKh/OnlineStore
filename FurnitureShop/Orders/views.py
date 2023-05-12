from django.shortcuts import render
from .models import OrderItem
from .forms import OrderPickupForm, OrderForm
from Cart.cart import Cart


def order_create(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            # очистка корзини
            cart.clear()

            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


def order_create_pickup(request):
    cart = Cart(request)

    if request.method == 'POST':
        form = OrderPickupForm(request.POST)

        if form.is_valid():
            order_pickup = form.save()

            for item in cart:
                OrderItem.objects.create(order_pickup=order_pickup, product=item['product'], price=item['price'], quantity=item['quantity'])
            # очистка корзини
            cart.clear()

            return render(request, 'orders/order/created.html', {'order': order_pickup})
    else:
        form = OrderPickupForm()

    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form, })

