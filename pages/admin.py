from .models import Ticket
from django.contrib import admin


class TicketAdmin(admin.ModelAdmin):
    fields = '__all__'
    readonly_fields = ['time_create']
    list_display = '__all__'
    list_display_links = ('name',)
    ordering = ['time_create']
    list_per_page = 10
    search_fields = ['name']
    save_on_top = True