from django.contrib import admin

# Register your models here.
from .models import Category,Sub_Category,Contact_us,Brand
from .models import Product,Person

admin.site.register(Person)
admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Product)
admin.site.register(Contact_us)
admin.site.register(Brand)
