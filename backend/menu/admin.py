from django.contrib import admin
from .models import Review, Category, Item, Country, ItemVariant

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Review)
admin.site.register(ItemVariant)
admin.site.register(Country)

# Register your models here.
