from django.contrib import admin
from django.urls import path
from CRUD.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', read, name='read'),
    path('create/', create, name='create'),
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
    path('view/<int:id>/', view, name='view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
