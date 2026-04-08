from django.contrib import admin
from .models import ActivityLog

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ['action_type', 'description', 'timestamp']
    list_filter = ['action_type']
    readonly_fields = ['action_type', 'description', 'content_type', 'object_id', 'timestamp']

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
