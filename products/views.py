from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# List all products
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/index_list.html", {"products": products})

# Add a new product
def product_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        image = request.FILES.get("image")

        Product.objects.create(
            name=name,
            description=description,
            price=price,
            stock=stock,
            image=image
        )
        return redirect('product_list')

    return render(request, "products/index.html")

# Update a product
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.name = request.POST.get("name")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        product.save()
        return redirect('product_list')

    return render(request, 'products/edit.html', {'product': product})

# Delete a product
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
    return redirect('product_list')
