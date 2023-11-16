from django.shortcuts import render
from django.http import HttpResponse  # Import HttpResponse

def get_product(request, slug):

    product = f"Product with slug: {slug}"

    return render(request, 'product/product.html', {'product': product})
