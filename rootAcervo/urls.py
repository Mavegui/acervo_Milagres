from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('chefinhoadmin/', admin.site.urls),
    path('', include('appAcervo.urls')),
]
