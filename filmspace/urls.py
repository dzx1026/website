from django.urls import path
from . import views

app_name = 'filmspace'
urlpatterns = [
    path('film/<int:film_id>/', views.getfilminfo, name='getfilminfo'),
]
