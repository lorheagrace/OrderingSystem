from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Products(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    name = models.CharField(max_length=255)
    variation_name = models.CharField(max_length=100, default='Default')  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True) 

    def __str__(self):
        return f"{self.name} - {self.variation_name}"

class OnlinePaymentDetails(models.Model):
    PLATFORM_CHOICES = [
        ('gcash', 'GCash'),
        ('paymaya', 'PayMaya'),
    ]

    platform = models.CharField(max_length=10, choices=PLATFORM_CHOICES)
    qr_image = models.ImageField(upload_to='qr_codes/')
    recipient_name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.get_platform_display()} - {self.recipient_name}"

class BusinessOwnerAccount(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Storing plain text password (NOT recommended in production)
    first_login = models.BooleanField(default=True)

    def __str__(self):
        return self.email

@receiver(post_migrate)
def create_default_business_owner(sender, **kwargs):
    if sender.name == 'MSMEOrderingWebApp':  # Replace YOUR_APP_NAME with your Django app's name
        BusinessOwnerAccount.objects.get_or_create(
            email='businessowner@gmail.com',
            defaults={
                'password': 'msme2025!',
                'first_login': True
            }
        )