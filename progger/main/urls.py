from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='register'),
    path('about', views.about, name='about'),
    path('add_register', views.add_register, name='add_register'),
    path('delete_register', views.delete_register, name='delete_register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

