from django.contrib import admin
from .models import ClientUser
class Userb(admin.ModelAdmin):
    list_display = ('id', 'firstnamear', 'lastnamear', 'phone', 'uid')
    list_filter = ('firstnamear', 'lastnamear')
    search_fields = ('firstnamear', 'lastnamear', 'phone', 'uid')  # Add search functionality

# Register the model and admin class
admin.site.register(ClientUser,Userb)
