from django.contrib import admin
from django.urls import path, re_path, include
from BooksWeb import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'BooksWeb'

urlpatterns = [
     path('admin/', admin.site.urls),
    path('', views.allbooks, name='Home'),
    path('book/feedback/<int:id_book>', views.feedbackbook, name='FeedBackBook'),

    path('book/<int:id_book>', views.detailbook, name='DetailInformationBooks'),
    path('feedback/', views.allfeeadbaks, name='filter_books')
    # path('', include('BooksWebApp.urls'))
    # #re_path - позволяет задать адреса URL с помощью регулярных выражений (к примеру откроется и localhost:8000/about и localhost:8000/about/asd )
    # re_path(r'^about/contact', views.contact, name='Contact'),
    # re_path(r'^about', views.about, name='About'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)