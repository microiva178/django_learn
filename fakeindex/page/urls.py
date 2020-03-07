from django.urls import path
from . import views
#from django.conf.urls import url

urlpatterns = [
    path('', views.page, name='page'),
    #url('', views.Page.as_view(), name='Page'),
]
