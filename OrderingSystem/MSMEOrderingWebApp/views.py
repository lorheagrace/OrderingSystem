from django.shortcuts import render, redirect, get_object_or_404
from .models import User, Products, ProductCategory
from django.contrib import messages
from django.db.models import Min, Max
from collections import defaultdict
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.core import serializers

def login_view(request):
    return render(request, 'MSMEOrderingWebApp/login.html', {
        'background_color': request.session.get('background_color', 'white'),
        'font_family': request.session.get('font_family', 'sans-serif'),
    })

def logout_view(request):
    return render(request, 'MSMEOrderingWebApp/login.html')

def register_user(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        city = request.POST['city']
        province = request.POST['province']
        zipcode = request.POST['zipcode']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'MSMEOrderingWebApp/register_user.html')

        if User.objects.filter(email=email).exists():
            return render(request, 'MSMEOrderingWebApp/register_user.html')

        user = User(
            first_name=first_name,
            last_name=last_name,
            contact_number=contact_number,
            email=email,
            city=city,
            province=province,
            zipcode=zipcode,
            password=password  # WARNING: Use hashing for real apps
        )
        user.save()
        return redirect('login')

    return render(request, 'MSMEOrderingWebApp/register_user.html')

def dashboard(request):
    return render(request, 'MSMEOrderingWebApp/dashboard.html')

def inventory(request):
    categories = ProductCategory.objects.all()
    products = Products.objects.all()

    if request.method == 'POST':
        if 'add_category' in request.POST:
            new_category = request.POST.get('new_category')
            if new_category:
                ProductCategory.objects.get_or_create(name=new_category)
                messages.success(request, "New category added.")
            return redirect('inventory')

        elif 'add_product' in request.POST:
            image = request.FILES.get('product_image')
            name = request.POST.get('product_name')
            category_id = request.POST.get('product_category')
            variation_names = request.POST.getlist('variation_name[]')
            variation_prices = request.POST.getlist('variation_price[]')

            if not name or not category_id:
                messages.error(request, "Product name and category are required.")
                return redirect('inventory')

            category = ProductCategory.objects.get(id=category_id)
            for vname, vprice in zip(variation_names, variation_prices):
                if vname.strip() and vprice.strip():
                    Products.objects.create(
                        category=category,
                        image=image,
                        name=name,
                        variation_name=vname,
                        price=vprice
                    )

            messages.success(request, "Product saved successfully.")
            return redirect('inventory')

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'MSMEOrderingWebApp/inventory.html', context)

def edit_product_price(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        new_price = request.POST.get('new_price')
        product = Products.objects.get(id=product_id)
        product.price = new_price
        product.save()
    return redirect('inventory')  # Adjust to your inventory view name

def delete_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect('inventory')

def toggle_availability(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    if request.method == 'POST':
        product.available = not product.available
        product.save()
    return redirect('inventory') 

def pos(request):
    products = Products.objects.select_related('category').filter(available=True)
    categories = ProductCategory.objects.all()

    grouped = defaultdict(list)
    for p in products:
        grouped[p.name].append(p)

    unique_products = []
    for name, group in grouped.items():
        min_price = min(p.price for p in group)
        max_price = max(p.price for p in group)
        category = group[0].category
        image = group[0].image

        unique_products.append({
            'name': name,
            'price_range': f"₱{min_price:.2f}" if min_price == max_price else f"₱{min_price:.2f} - ₱{max_price:.2f}",
            'category': category.name,
            'image': image,
        })

    return render(request, 'MSMEOrderingWebApp/pos.html', {
        'products': unique_products,
        'categories': categories,
        'all_products': list(products.values('name', 'variation_name', 'price')),  # use this for json_script
    })

def pos_cart_view(request):
    return render(request, 'MSMEOrderingWebApp/pos_cart.html')

def delivery(request):
    return render(request, 'MSMEOrderingWebApp/delivery.html')

def reviews(request):
    return render(request, 'MSMEOrderingWebApp/reviews.html')

def users(request):
    return render(request, 'MSMEOrderingWebApp/users.html')

def settings(request):
    return render(request, 'MSMEOrderingWebApp/settings.html')

def business_notifications(request):
    return render(request, 'MSMEOrderingWebApp/business_notification.html')

def customer_home(request):
    products = Products.objects.select_related('category').all()
    categories = ProductCategory.objects.all()

    grouped = defaultdict(list)
    for p in products:
        grouped[p.name].append(p)

    unique_products = []
    for name, group in grouped.items():
        min_price = min(p.price for p in group)
        max_price = max(p.price for p in group)
        category = group[0].category
        image = group[0].image

        unique_products.append({
            'name': name,
            'price_range': f"₱{min_price:.2f}" if min_price == max_price else f"₱{min_price:.2f} - ₱{max_price:.2f}",
            'category': category.name,
            'image': image,
        })

    return render(request, 'MSMEOrderingWebApp/customer_home.html', {
        'products': unique_products,
        'categories': categories,
        'all_products': list(products.values('name', 'variation_name', 'price')),  # use this for json_script
    })

def customer_reviews(request):
    return render(request, 'MSMEOrderingWebApp/customer_reviews.html')

def customer_cart(request):
    return render(request, 'MSMEOrderingWebApp/customer_cart.html')

def customer_checkout(request):
    return render(request, 'MSMEOrderingWebApp/customer_checkout.html')

def customer_notifications(request):
    return render(request, 'MSMEOrderingWebApp/customer_notification.html')

def customer_profile(request):
    return render(request, 'MSMEOrderingWebApp/customer_profile.html')

def online_payment_details(request):
    return render(request, 'MSMEOrderingWebApp/onlinepayment_details.html')

def change_password(request):
    return render(request, 'MSMEOrderingWebApp/change_password.html')