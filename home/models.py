from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):

    

    name = models.CharField(max_length=100)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    description = models.TextField()

    image = models.URLField()

    category = models.CharField(max_length=100)

    stock = models.IntegerField(default=0)

    available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Create your models here.
class Order(models.Model):

    
    PAYMENT_CHOICES = [
        ('UPI', 'UPI'),
        ('COD', 'Cash On Delivery'),
        ('NETBANKING', 'Net Banking'),
    ]
     
     ##########

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Delivered', 'Delivered'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    product_name = models.CharField(max_length=200)

    quantity = models.IntegerField()

    total_price = models.IntegerField()

    customer_name = models.CharField(max_length=200)

    phone = models.CharField(max_length=20)

    address = models.TextField()

    ordered_at = models.DateTimeField(auto_now_add=True)

    # NEW FIELDS

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    is_received = models.BooleanField(default=False)

    ###############

    
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    

    customer_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    product_name = models.CharField(max_length=100)

    quantity = models.FloatField()

    price_per_kg = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_CHOICES
    )

    ordered_at = models.DateTimeField(
        auto_now_add=True
    )
    buyer_state = models.CharField(
    max_length=100,
    null=True,
    blank=True
)

    buyer_district = models.CharField(
    max_length=100,
    null=True,
    blank=True
)

    buyer_mandal = models.CharField(
    max_length=100,
    null=True,
    blank=True
)

    buyer_village = models.CharField(
    max_length=100,
    null=True,
    blank=True
)

    status = models.CharField(
    max_length=20,
    default='Pending'
)

    accepted_by = models.CharField(
    max_length=100,
    null=True,
    blank=True
)

    seller_id = models.CharField(
    max_length=50,
    null=True,
    blank=True
)

    seller_name = models.CharField(
    max_length=100,
    null=True,
    blank=True



)
    
    ###################

    

    seller_name = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    seller_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    seller_address = models.TextField(
        blank=True,
        null=True
    )

    seller_latitude = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    seller_longitude = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    
    ###################

    def __str__(self):
        return self.customer_name


class Seller(models.Model):

    seller_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    seller_name = models.CharField(max_length=100)

    age = models.IntegerField()

    photo = models.ImageField(
        upload_to='seller_photos/'
    )
    aadhaar_number = models.CharField(
        max_length=12
    )

    phone_number = models.CharField(
        max_length=15
    )

    state = models.CharField(max_length=100)

    district = models.CharField(max_length=100)

    mandal = models.CharField(max_length=100)

    village = models.CharField(max_length=100)

    market_name = models.CharField(max_length=200)

    vegetables_selling = models.TextField()

    experience = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    ############
    latitude = models.CharField(
    max_length=100,
    blank=True,
    null=True
)

    longitude = models.CharField(
    max_length=100,
    blank=True,
    null=True
)
    ##########3

    def save(self, *args, **kwargs):

        if not self.seller_id:

            self.seller_id = (
                'FVS-' + str(uuid.uuid4())[:8]
            ).upper()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.seller_name
    

######3
class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    #issue = models.TextField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
##############        