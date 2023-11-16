from django.shortcuts import render
from django.http import HttpResponse

from products.models import Product  # Import HttpResponse

def get_product(request, slug):

    product = f"Product with slug: {slug}"
    # product = Product.objects.get(slug =slug)

    return render(request, 'product/product.html', {'product': product})
