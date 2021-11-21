from django.urls import path

from . import views

#import ackend.api.views as backendViews

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    #path('public_interface', backendViews.CertificatetListView.as_view(), name='public_interface')
    path('webportal', views.webportal, name='webportal'),
]
