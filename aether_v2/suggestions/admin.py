from django.contrib import admin
from .models import Suggestion

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'is_read', 'created_at']
    list_editable = ['is_read']
    readonly_fields = ['name', 'message', 'created_at']
