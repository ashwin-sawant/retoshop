from django.contrib import admin
from Users.models import UserDetails

class UserAdmin(admin.ModelAdmin):
    list_display = ('Username','Email','Password')

admin.site.register(UserDetails,UserAdmin)
