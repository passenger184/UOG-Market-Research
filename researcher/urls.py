from  django.urls import path
from . import views


urlpatterns = [
    path('', views.research, name='research'),
    path('main', views.main, name='main'),
    path('table', views.table, name='table'),
    path('setup', views.setup, name='setup'),
    path('add_setup', views.add_setup, name='add_setup'),
    path('request', views.request, name='request'),
    path('search', views.search, name='search'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete_product, name='delete'),


    path('send_request', views.send_request, name='send_request'),
]
