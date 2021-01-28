from django.contrib import admin
from .models import Form


@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'email')
    list_filter = ['created_on']
    search_fields = ('name', 'email', 'body')
