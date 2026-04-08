from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import LinkCategory, Link

@cache_page(60 * 15)
def link_list(request):
    categories = LinkCategory.objects.prefetch_related('links').order_by('order', 'name')
    uncategorized = Link.objects.filter(category=None)
    return render(request, 'links/list.html', {
        'categories': categories,
        'uncategorized': uncategorized,
    })
