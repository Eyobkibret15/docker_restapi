from django.contrib import admin

# Register your models here.

from .models import country, city, hotel

admin.site.register(country)
admin.site.register(city)
admin.site.register(hotel)
