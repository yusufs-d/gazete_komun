"""myblog_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from article import views
from article.views import dashboard
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('create_about/',views.create_about,name ="create_about"),
    path('about/',views.about,name ="about"),
    path('siyaset-yazi/',views.siyaset_yazi,name = "siyaset-yazi"),
    path('siyaset-haber/',views.siyaset_haber,name = "siyaset-haber"),
    path('articles/',include("article.urls")),
    path('user/',include('user.urls')),
    path('dashboard/',dashboard,name="dashboard"),
    path('spor-yazi/',views.spor_yazi,name = "spor-yazi"),
    path('spor-yazilar/',views.spor_haber,name = "spor_haber"),
    path('müzik/',views.muzik,name = "muzik"),
    path('sinema/',views.sinema,name = "sinema"),
    path('edebiyat/',views.edebiyat,name = "edebiyat"),
    path('sahne-sanatlari/',views.sahne,name = "sahne_sanatlari"),
    path('gorsel-sanatlar/',views.gorsel,name = "gorsel"),
    path('gezi-notu/',views.gezi,name = "gezi"),
    path('ceviri/',views.ceviri,name = "ceviri"),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
