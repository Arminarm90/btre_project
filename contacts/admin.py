from django.contrib import admin
from .models import Contacts


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing',
                    'email', 'message')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'email', 'listing')
    list_per_page = 25


admin.site.register(Contacts, ContactAdmin)
