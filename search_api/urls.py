from django.conf.urls import url

from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('import/', views.data_import, name="import-data"),
    path('<str:msg>/', views.data_view_details, name="search"),
    # url(r'^search/queryset=(?P<msg>[\w ]+)/$', views.data_view_details_msg, name="msg search"),
]
