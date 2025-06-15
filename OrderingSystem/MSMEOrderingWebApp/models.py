from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=10)
    password = models.CharField(max_length=128)  # We'll hash it manually

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

    def __str__(self):
        return f"{self.name} - {self.variation_name}"
    
    