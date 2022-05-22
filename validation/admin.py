from lib2to3.pytree import Base
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model

#Remove group model from admin.
# admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    #The forms to add and change user instances
    form  = UserAdminChangeForm
    add_form = UserAdminChangeForm

    #The fields to be used i displaying the user model
    #These override the definitions on the base UserAdmin
    #that reference specific fields on auth user
    list_display = ['email', 'admin']
    list_filter = ['admin', 'staff','is_sponsor', 'is_student']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_student', 'is_sponsor', 'is_active')}),
    )
    #add fieldsets is not a standard ModelAdmin attribute. UserAdmin
    #overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields' : ('email', 'password', 'password2')}
            ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
