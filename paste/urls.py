from django.urls import path
from .views import root


urlpatterns = [
    path('', root),
    path('<int:idf>/', root),
    path('<str:username>/', root),
]