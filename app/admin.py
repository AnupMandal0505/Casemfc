# your_app/admin.py

from django.contrib import admin
from .models import ContactMessage,Company


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'subject', 'datetime', 'status')
    list_filter = ('status', 'datetime')
    search_fields = ('fullname', 'email', 'subject', 'message')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address', 'city', 'state', 'country', 
        'phone_number', 'email', 'founded_date', 
        'is_active', 'mission', 'vision'
    )
    search_fields = ('name', 'address', 'city', 'state', 'country', 'email', 'mission', 'vision')
    list_filter = ('is_active', 'founded_date')
