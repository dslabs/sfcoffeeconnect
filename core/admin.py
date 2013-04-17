from django.contrib import admin
from core.models import CoffeeMatch

class CoffeeMatchAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]
    list_display = ["recipient", "candidate", "accepted", "updated"]
    list_filter = ["accepted", "updated", "recipient", "candidate"]
    search_fields = ["recipient", "candidate"]
    fieldsets = [
        ("Meta", {"fields": ["created", "updated"]}),
        ("People", {"fields": ["recipient", "candidate"]}),
        ("Status", {"fields": ["accepted"]}),
    ]

admin.site.register(CoffeeMatch, CoffeeMatchAdmin)
