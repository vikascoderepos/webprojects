from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'gender', 'bio', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'phone_number', 'created_date', 'is_parent', 'is_teacher']