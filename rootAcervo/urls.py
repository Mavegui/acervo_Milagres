from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chefinhoadmin/', admin.site.urls),
    path('', include('appAcervo.urls')),
]
