from django.contrib import admin
from .models import contract

class contractAdmin(admin.ModelAdmin):
    list_display = ['clientName','dealer','clientNumber',]


admin.site.register(contract , contractAdmin)