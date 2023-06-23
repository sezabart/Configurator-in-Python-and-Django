#from django.conf.urls import url  #deprecated
from django.urls import re_path as url
from . import views
app_name = 'oferty' #added to solve app/urls.py problem

urlpatterns = [
    url(r'^tworz/$',
        views.order_create,
        name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$',
        views.admin_order_pdf,
        name='admin_order_pdf'),
]
