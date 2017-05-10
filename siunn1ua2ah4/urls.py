"""siunn1ua2ah4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.views.static import serve


# from django.contrib import admin
urlpatterns = [
    url(r'^', include('line回應.網址')),
    url(r'^資料庫影音檔案/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT, 'show_indexes': False
    }),
    #     url(r'^admin/', admin.site.urls),
]
