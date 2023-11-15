from django.contrib import admin

# Register your models here.
from .models import Customer, Container, Item


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number')


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'size', 'available', 'start_date', 'end_date',)
    list_filter = ('size', 'available')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_filter = ('type',)
