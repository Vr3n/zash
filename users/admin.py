from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm
from .models import Profile, CustomUser

# Custom Admin Class.


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {
            "fields": (
                'username',
                'email',
                'password',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_admin',
            ),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username', 'email')
    filter_horizontal = ()


# Register your models here.
admin.site.register(Profile)
admin.site.register(CustomUser, UserAdmin)

# Unregister to override Custom User Model.
admin.site.unregister(Group)
