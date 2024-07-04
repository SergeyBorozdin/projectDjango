from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='register'),
    path('about', views.about, name='about'),
    path('add_register', views.add_register, name='add_register'),
    path('edit_register', views.edit_register, name='edit_register'),
    path('<int:pk>', views.RegisterRecordView.as_view(), name='record-detail'),
    path('<int:pk>/update', views.RegisterRecordUpdate.as_view(), name='record-update'),
    path('<int:pk>/delete', views.RegisterRecordDelete.as_view(), name='record-delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register_user/', views.register_user, name='register_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

