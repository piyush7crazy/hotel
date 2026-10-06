from django.contrib import admin
from .models import Room , Customer , Booking , Invoice


admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Booking)
admin.site.register(Invoice)