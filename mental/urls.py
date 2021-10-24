from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('radio/', include('radio.urls')),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('about/',  include('about.urls')),
    path('my_account/',  include('my_account.urls')),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

]

urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)