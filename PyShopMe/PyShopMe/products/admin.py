from django.contrib import admin
from.models import Product
from.models import Offer



# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'stock', 'price','description')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')

admin.site.register(Product, ProductAdmin)
admin.site.register(Offer, OfferAdmin)