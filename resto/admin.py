from django.contrib import admin
from resto.models import ContactMessage
# Register your models here.


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone',
                    'subject', 'message', 'date_sent'
                    ]
    search_fields = ['name', 'email']


admin.site.register(ContactMessage, ContactMessageAdmin)
