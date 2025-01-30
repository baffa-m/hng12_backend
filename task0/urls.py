from django.urls import path
from .views import info

urlpatterns = [
    path('task0', info),
]