from django.contrib import admin
from .models import Deserts, Order, Drinks

admin.site.register(Order)
admin.site.register(Deserts)
admin.site.register(Drinks)

