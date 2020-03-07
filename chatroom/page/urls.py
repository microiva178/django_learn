from django.urls import path
from . import views

urlpatterns = [
    #path('', views.page, name='page'),
    path('', views.message, name='message'),
    path('accounts/profile/', views.REDIRECT, name='REDIRECT')

]