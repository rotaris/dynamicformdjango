from django.contrib import admin
from models import List, Item


class ItemInline(admin.StackedInline):
    model = Item
    extra = 1
    
class ListAdmin(admin.ModelAdmin):
    inlines = [ItemInline]
    
admin.site.register(List, ListAdmin)