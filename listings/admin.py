from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_publishred',
                    'price', 'list_Date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'is_publishred')
    list_editable = ('is_publishred',)
    search_fields = ('title', 'description', 'address',
                     'city', 'zipcode', 'price')
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)
