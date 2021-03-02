from .views import usergame_list
from .views import userevent_list
from django.urls import path

urlpatterns = [
    path('reports/usergames', usergame_list),
    path('reports/userevents', userevent_list),
]
