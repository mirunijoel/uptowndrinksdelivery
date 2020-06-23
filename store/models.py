from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# //////////////////...........Customer model...........\\\\\\\\\\\\\\\\\\\
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# //////////////////...........Product model...........\\\\\\\\\\\\\\\\\\\
class Product(models.Model):
    PRODUCT_CHOICES = (
        ('Whisky', (
                    ('BLENDED SCOTCH', 'BLENDED SCOTCH',),
                    ('BOURBON WHISKIES', 'BOURBON WHISKIES',),
                    ('IRISH WHISKIES', 'IRISH WHISKIES',),
                    ('SINGLE MALT', 'SINGLE MALT',),
                    ('TENESEE WHISKIES', 'TENESEE WHISKIES',),
                )
            ),
        ('vodka', 'vodka',),
        ('Wine', (
                    ('RED WINE', 'RED WINE',),
                    ('WHITE WINE', 'WHITE WINE',),
                    ('ROSE WINE', 'ROSE WINE',),
                )
            ),
        ('Champagne', 'Champagne',),
        ('Brandy', 'Brandy',),
        ('Cognac', 'Cognac',),
        ('Beer', (
                    ('CIDER', 'CIDER',),
                    ('LAGER', 'LAGER',),
                    ('MALT', 'MALT',),
                    ('DRAUGHT', 'DRAUGHT',),
                )
            ),
        ('Tequila', 'Tequila',),
        ('Rum', 'Rum',),
        ('Gin', 'Gin',),
        ('Liquer', 'Liquer',),
        ('Extras', 'Extras',),
    )
    product_type = models.CharField(max_length=255, choices=PRODUCT_CHOICES, default=None)
    picture = models.ImageField(upload_to='Uploads', height_field=None, default=None, width_field=None, max_length=None)
    name = models.CharField(max_length=200, default=None)
    capacity = models.CharField(max_length=200)
    cash = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    date_uploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.picture.url
        except:
            url = ''
        return url


# //////////////////...........order model...........\\\\\\\\\\\\\\\\\\\
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    date_ordered = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


# //////////////////...........orderItem model...........\\\\\\\\\\\\\\\\\\\
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.cash * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=True)
    phone =models.CharField(max_length=12, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
