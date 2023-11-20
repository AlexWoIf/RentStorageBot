from django.contrib import admin

# Register your models here.
from .models import Customer, Container, Reservation, Delivery, Step, Button, Session


class StepAdminInline(admin.TabularInline):
    model = Step.buttons.through


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
    inlines = [StepAdminInline]


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_filter = ('text', )


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_filter = ('user', )
    list_display = ('user', 'get_telegram_id')
    readonly_fields = ('get_telegram_id',)

    def get_telegram_id(self, obj):
        return obj.user.telegram_id

    get_telegram_id.short_description = 'Telegram ID'

