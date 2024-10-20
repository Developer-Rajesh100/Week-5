from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('musician/', include('musician.urls')),
    path('album/', include('album.urls')),
    path('auth/', include('authentication.urls'))
]
