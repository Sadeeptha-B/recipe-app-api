from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# To convert strings to human readable text to support multiple languages (setting up translation files)
from django.utils.translation import gettext as _
from core import models

# Using the default django user admin and changing some 
# variables. 
class UserAdmin(BaseUserAdmin):
    # Order the list by ID and list out the email and name
    ordering = ['id']
    list_display = ['email', 'name']

    # The fieldsets for the change and create page
    # Each bracket is a section which has a section title and fields
    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        # For just one field, you need to provide the comma, else it 
        # just be understood as a string
        # The _ is for the translation 
        (_('Personal Info'), {'fields':('name',)}),

        # Permissions section
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )

    # Fieldsets for the create user page
    add_fieldsets = (
        # classes assigned to the form. Defaults taken from Django-admin documentation
        # Include the comma at the end since one item only
        (None, {
            'classes':('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)

# To view this in the browser we need to set up our db
