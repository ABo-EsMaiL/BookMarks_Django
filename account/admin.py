from django.contrib import admin
from .models import Profile


# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'date_birth', 'photo']
    search_fields = ['user__username', 'phone_number']
    list_filter = ['date_birth']
    date_hierarchy = 'date_birth'
    list_per_page = 5
    
    raw_id_fields = ['user']