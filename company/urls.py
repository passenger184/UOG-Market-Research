from  django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('company', views.company, name='company'),
    path('companyinfo', views.companyinfo, name='companyinfo'),
    path('agree', views.agree, name='agree'),
    path('response/<int:pk>/', views.response, name='response'),
    path('update_response/<int:pk>/', views.update_response, name='update_response'),
    path('home', views.index, name='index'),
]








