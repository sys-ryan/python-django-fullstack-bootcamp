from django.conf.urls import url
from second_app import views

urlpatterns = [
    url('', views.index, name='index'),
]