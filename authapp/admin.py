from django.contrib import admin
from authapp import models

# Register your models here.


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "first_name",
                    "last_name", "email"]
