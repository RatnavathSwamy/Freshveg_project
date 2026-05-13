from django.contrib import admin
from .models import Product, Contact,Order
from .models import ContactMessage



admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(ContactMessage)


# Register your models here.

