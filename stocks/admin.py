from django.contrib import admin
from .models import Stock, Buys

# Register your models here.
admin.site.register(Stock)
admin.site.register(Buys)