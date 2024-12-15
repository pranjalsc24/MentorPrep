
from django.contrib import admin
from django.urls import path,include
# from django.contrib.staticfiles import 
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from studyapp.settings import MEDIA_URL,STATIC_URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('api/',include('base.api.urls'))
]
# urlpatterns += staticfiles_urlpatterns(MEDIA_URL,STATIC_URL)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
