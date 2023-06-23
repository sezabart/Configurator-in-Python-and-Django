from django.urls import re_path as url
from . import views
app_name = 'konfigurator' #added to solve app/urls.py problem

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
]
