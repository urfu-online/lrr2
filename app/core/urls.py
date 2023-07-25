from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('passport/<str:passport_id>/', views.passport, name='passport'),
    path('myresources/', views.myresources, name='myresources'),
    path('myrequests/', views.myrequests, name='myrequests'),
]
