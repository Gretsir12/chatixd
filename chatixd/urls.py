from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('chat.urls')),
    path('reg/', include('registration.urls')),
]