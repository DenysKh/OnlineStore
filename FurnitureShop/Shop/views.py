from django.shortcuts import render, get_object_or_404

from Cart.forms import CartAddProductForm
from .models import Room, Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def home(request):
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
    }

    return render(request, 'shop/home.html', context)


def product_list(request, room_slug=None, category_slug=None):
    category = None
    rooms = Room.objects.all()
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
    else:
        products = Product.objects.all()

    # Сортування
    sort_by = request.GET.get('sort_by')
    if sort_by == 'newest':
        products = products.order_by('-created')
    if sort_by == 'oldest':
        products = products.order_by('created')
    if sort_by == 'ascending':
        products = products.order_by('price')
    elif sort_by == 'descending':
        products = products.order_by('-price')

    # Пагінація
    paginator = Paginator(products, 12)  # Кількість продуктів на одній сторінці
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    total_products = paginator.count

    context = {
        'rooms': rooms,
        'current_room': room,
        'category': category,
        'categories': categories,
        'products': products,
        'total_products': total_products,
    }

    return render(request, 'shop/product/list.html', context)


def search(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(Q(name__icontains=query))
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'shop/product/search.html', context)


def about(request):
    return render(request, 'shop/about.html')


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }

    return render(request, 'shop/product/detail.html', context)
