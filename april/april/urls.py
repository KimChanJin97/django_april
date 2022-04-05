from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('word_counter.urls')), # https://도메인/result
    path('admin/', admin.site.urls),
]
