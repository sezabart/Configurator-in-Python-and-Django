#from django.conf.urls import include, url #deprecated
from django.urls import include
from django.urls import re_path as url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_title = "Test"
admin.site.site_header = "Konfigurator"
admin.site.index_title = "Administracja stroną"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^oferty/', include(('oferty.urls'), namespace='oferty')),
    url(r'^', include(('konfigurator.urls'), namespace='konfigurator'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
