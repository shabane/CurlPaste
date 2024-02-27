from django.urls import path
from .views import root, file_serv


urlpatterns = [
    path('', root),
    path('<int:idf>/', root),
    path('<str:username>/', root),
    path('file/<str:path>/', file_serv),
]