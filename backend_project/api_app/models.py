from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class ProductModel(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product/', blank=True, null=True)

    @property
    def in_stock(self):
        return self.stock > 0
    
    def __str__(self):
        return self.name 
    
class OrderModel(models.Model):
    class statusChoice(models.TextChoices):
        PENDING = 'pending'
        CONFIRMED  = 'confirmed'
        CANCELLED = 'cancelled' 

    order_id = models.UUIDField(primary_key=True,default=uuid.uuid4)  
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=10, choices=statusChoice.choices, default=statusChoice.PENDING)
    products = models.ManyToManyField(ProductModel,through='OrderItem',related_name='order')

    def __str__(self):
        return f"Order {self.order_id} by {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE,related_name='items') 
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE) 
    quantity = models.PositiveIntegerField()  

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} X {self.product.name} order No {self.order.order_id}"



    

