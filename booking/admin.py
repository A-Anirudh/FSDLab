from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Bookings)
# admin.site.register(Passenger)
admin.site.register(Driver)


@admin.register(Passenger)
class passengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email','number']
    ordering = ['-email']
    search_fields = ['name','email']
    fields = ['email']
    list_filter = ['name','number']