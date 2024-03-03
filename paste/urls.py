from django.urls import path
from .views import root, file_serv, ping


urlpatterns = [
    path('', root),
    path('<int:idf>/', root),
    path('<int:idf>', root),
    path('<str:username>/', root),
    path('<str:username>', root),
    path('file/<str:path>/', file_serv),
    path('file/<str:path>', file_serv),
]