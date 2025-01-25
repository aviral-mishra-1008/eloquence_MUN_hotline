from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import User, Message

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'country', 'is_eb', 'is_active')
    list_filter = ('is_eb', 'is_active')
    search_fields = ('username', 'country')
    ordering = ('country',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'country', 'flag', 'is_eb', 'is_active'),
        }),
    )

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('MUN Information', {'fields': ('country', 'flag', 'is_eb')}),
        ('Permissions', {'fields': ('is_active',)}),
    )

    def save_model(self, request, obj, form, change):
        if not change: 
            if obj.is_eb:
                obj.is_staff = True
        super().save_model(request, obj, form, change)

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Message)
admin.site.unregister(Group)