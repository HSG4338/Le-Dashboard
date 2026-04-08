from django.shortcuts import render
from .models import ActivityLog

def activity_feed(request):
    logs = ActivityLog.objects.all()[:50]
    return render(request, 'activity/feed.html', {'logs': logs})
