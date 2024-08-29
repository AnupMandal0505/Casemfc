# your_app/admin.py

from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email', 'phone', 'subject', 'datetime', 'status')
    list_filter = ('status', 'datetime')
    search_fields = ('fullname', 'email', 'subject', 'message')
