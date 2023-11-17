from django.contrib import admin

# Register your models here.
from .models import Customer, Container, Reservation, Delivery, Step, Button, Session


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'phone_number')


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'size', 'available', )
    list_filter = ('size', 'available')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_filter = ('customer', )


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_filter = ('date', )


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_filter = ('name', )


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_filter = ('text', )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_filter = ('user', )
