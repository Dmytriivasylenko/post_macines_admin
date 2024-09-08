from django.contrib import admin
from parcel.models import Parcel
from post_machine.models import PostMachine, Locker


class ParcelAdmin(admin.ModelAdmin):
    # Відображаємо основні поля в адмінці
    list_display = ('recipient', 'sender', 'post_machine_recipient', 'status', 'order_datetime', 'update_datetime')

    # Додаємо можливість фільтрувати за статусом та часом замовлення
    list_filter = ('status', 'order_datetime', 'post_machine_recipient')

    # Додаємо поле пошуку за ім'ям відправника та одержувача
    search_fields = ('sender', 'recipient__username')

    # Робимо поля доступними для зміни через інтерфейс
    fields = (
    'recipient', 'sender', 'size', 'post_machine_recipient', 'locker', 'order_datetime', 'update_datetime', 'status')


admin.site.register(Parcel, ParcelAdmin)


class PostMachineAdmin(admin.ModelAdmin):
    list_display = ('adress', 'city')  # Відображаємо поля "Адреса" та "Місто"
    search_fields = ('adress', 'city')  # Додаємо можливість пошуку за адресою та містом

class LockerAdmin(admin.ModelAdmin):
    list_display = ('size', 'post_machine_recipient_id', 'status')  # Відображаємо розмір, постамат і статус
    list_filter = ('status', 'size')  # Фільтр за статусом і розміром
    search_fields = ('post_machine_recipient_id__adress', 'post_machine_recipient_id__city')

admin.site.register(PostMachine, PostMachineAdmin)
admin.site.register(Locker, LockerAdmin)