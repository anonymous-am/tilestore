from django.db import models

# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category_id = models.CharField(max_length=50, unique=True)
    category_image = models.ImageField(upload_to='img/', default=None)

    def __str__(self):
        return self.category_id


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    size = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, to_field='category_id')

    # category = models.CharField(max_length=50)
    product_details = models.TextField()
    product_image = models.ImageField(upload_to='product_images/', default=None)


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=50)
    product_id = models.CharField(max_length=50)
    merchant_name = models.CharField(max_length=255)
    merchant_mobile_no = models.CharField(max_length=15)
    seller_id = models.CharField(max_length=50,default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    user_comment = models.TextField(null=True, blank=True)
    order_date = models.DateField()
    
    mail_status = models.BooleanField(default=False)
    ORDER_PROCESSED_CHOICES = [
        ('0', 'Pending'),
        ('1', 'Confirmed'),
        ('2', 'Delivered'),
        ('3', 'Cancelled'),
    ]
    order_processed = models.CharField(max_length=20, choices=ORDER_PROCESSED_CHOICES, default='pending')

