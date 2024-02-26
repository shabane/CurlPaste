from django.urls import path
from .views import root


urlpatterns = [
    path('', root)
]