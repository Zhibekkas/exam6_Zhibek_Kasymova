from django.contrib import admin
from webapp.models import Guest
# Register your models here.


class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'text', 'creation_date', 'edition_date', 'status']
    list_filter = ['status']
    search_fields = ['name', 'email']
    fields = ['name', 'email', 'text', 'creation_date', 'edition_date', 'status']
    readonly_fields = ['creation_date', 'edition_date']


# Register your models here.
admin.site.register(Guest, GuestAdmin)
