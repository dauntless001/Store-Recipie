from django.contrib import admin
from django.contrib.auth import admin as u_admin
from base.models import User
from django.utils.translation import gettext_lazy as _
# Register your models here.
@admin.register(User)
class UserAdmin(u_admin.UserAdmin):
    list_display = ['email', 'first_name', 'last_name']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': (
            'first_name', 'last_name', 
            'email', 'sex', 'marital_status', 'nationality','image'
            )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )