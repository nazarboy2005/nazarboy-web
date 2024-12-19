from django.contrib import admin
from .models import ContactInfoModel, TelegramDetailsModel


@admin.register(ContactInfoModel)
class ContactInfoModelAdmin(admin.ModelAdmin):
    list_display = ['email_address', 'phone_number']

@admin.register(TelegramDetailsModel)
class TelegramDetailsModelAdmin(admin.ModelAdmin):
    list_display = ['token', 'telegram_id']