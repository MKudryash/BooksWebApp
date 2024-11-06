"""
URL configuration for BooksWebApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path, include
from BooksWeb import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
     path('admin/', admin.site.urls),
    # path('', views.allbooks, name='Home'),
    # path('book/<int:id_book>', views.detailbooks, name='DetailInformationBooks'),
     path('', include('BooksWeb.urls'))
    # #re_path - позволяет задать адреса URL с помощью регулярных выражений (к примеру откроется и localhost:8000/about и localhost:8000/about/asd )
    # re_path(r'^about/contact', views.contact, name='Contact'),
    # re_path(r'^about', views.about, name='About'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
