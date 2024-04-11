from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.menu),
    re_path(r'^tree/.+', views.menu, name='menu'),
]
