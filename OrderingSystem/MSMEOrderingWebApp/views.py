from django.shortcuts import render

def login_view(request):
    return render(request, 'MSMEOrderingWebApp/login.html')

def logout_view(request):
    return render(request, 'MSMEOrderingWebApp/login.html')

def register_user(request):
    return render(request, 'MSMEOrderingWebApp/register_user.html')

def dashboard(request):
    return render(request, 'MSMEOrderingWebApp/dashboard.html')

def inventory(request):
    return render(request, 'MSMEOrderingWebApp/inventory.html')

def pos(request):
    return render(request, 'MSMEOrderingWebApp/pos.html')

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
    return render(request, 'MSMEOrderingWebApp/customer_home.html')

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

