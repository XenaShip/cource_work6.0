from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'country', 'avatar',)
    list_filter = ('email', 'phone',)
    search_fields = ('email', 'phone', 'country',)
