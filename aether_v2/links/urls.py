from django.urls import path
from . import views
urlpatterns = [
    path('links/', views.link_list, name='link_list'),
]
