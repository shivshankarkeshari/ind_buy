from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('search', views.data_view_details, basename='asd')


urlpatterns = [
    path('import/', views.data_import, name="import-data"),
    # path('api/', include(router.urls)),
    path('search/<str:msg>/', views.data_view_details, name="search"),
]