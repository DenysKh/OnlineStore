from django.shortcuts import render, get_object_or_404

from Cart.forms import CartAddProductForm
from .models import Room, Category, Product


def home(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }

    return render(request, 'shop/home.html', context)


def product_list(request, room_slug=None, category_slug=None):
    category = None
    room = None
    categories = None
    products = None

    if room_slug:
        room = get_object_or_404(Room, slug=room_slug)
        categories = Category.objects.filter(room=room)
        products = Product.objects.filter(category__room=room, available=True)

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

    context = {
        'current_room': room,
        'category': category,
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'shop/product/detail.html', context)
