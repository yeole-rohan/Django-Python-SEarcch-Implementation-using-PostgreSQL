from django.contrib import admin
from .models import RestaurantDetails,RestaurantAddress
# Register your models here.
admin.site.register(RestaurantDetails)
admin.site.register(RestaurantAddress)