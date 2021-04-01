from django.db import models
# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=200,null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return "accounts/customer/%i/" %self.id
class Tag(models.Model):
    name= models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Out Door','Out Door'),
    )
    Type = (
        ('Each','each'),
        ('KG','kg'),
    )
    name=models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    Product_type = models.CharField(max_length=200,null=True,choices=Type)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    quantity=models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product.name
