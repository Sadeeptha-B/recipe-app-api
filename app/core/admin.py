from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models

# Using the default django user admin and changing some 
# variables. 
class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


admin.site.register(models.User, UserAdmin)

# To view this in the browser we need to set up our db
