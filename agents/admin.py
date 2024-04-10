from django.contrib import admin
from .models import Member

# Register your models here.
@admin.register(Member)
class saket(admin.ModelAdmin):
    list_display = ('firstName', 'lastName')

#admin.site.register(Member)

