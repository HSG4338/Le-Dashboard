from django.shortcuts import render, get_object_or_404
from .models import Project, Tag


def home(request):
    projects = Project.objects.prefetch_related('tags').order_by('-updated_at')[:6]
    from activity.models import ActivityLog
    recent = ActivityLog.objects.order_by('-timestamp')[:8]
    return render(request, 'home.html', {'projects': projects, 'recent_activity': recent})


def project_list(request):
    status_filter = request.GET.get('status', '')
    tag_filter = request.GET.get('tag', '')
    qs = Project.objects.prefetch_related('tags')
    if status_filter:
        qs = qs.filter(status=status_filter)
    if tag_filter:
        qs = qs.filter(tags__slug=tag_filter)
    if request.headers.get('HX-Request'):
        return render(request, 'projects/_grid.html', {'projects': qs})
    return render(request, 'projects/list.html', {
        'projects': qs,
        'tags': Tag.objects.all(),
        'status_filter': status_filter,
        'tag_filter': tag_filter,
        'status_choices': Project.STATUS_CHOICES,
    })


def project_detail(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related('tags'), slug=slug)
    return render(request, 'projects/detail.html', {'project': project})
