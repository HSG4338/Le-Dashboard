from django.urls import path
from . import views
urlpatterns = [
    path('suggestions/', views.suggestion_form, name='suggestions'),
]
