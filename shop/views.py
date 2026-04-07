from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator
from django.db.models import Q
from cart.form import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    query = request.GET.get('q', '').strip()
    sort = request.GET.get('sort')

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'name_asc':
        products = products.order_by('name')
    elif sort == 'name_desc':
        products = products.order_by('-name')
    else:
        products = products.order_by('name')

    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    products_page = paginator.get_page(page_number)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products_page,
        'query': query,
        'current_sort': sort,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    if request.method == 'POST':
        cart_product_form = CartAddProductForm(request.POST)
        if cart_product_form.is_valid():
            cart_product_form.save()
    categories = Category.objects.all()
    return render(request, 'shop/product/detail.html', {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form
    })