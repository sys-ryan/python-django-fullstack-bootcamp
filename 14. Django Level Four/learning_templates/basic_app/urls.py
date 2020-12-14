from django.urls import path
# from django.conf.urls import include
from basic_app import views


# TEMPLATE TA GGING
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
