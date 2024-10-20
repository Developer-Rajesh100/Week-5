from django.urls import path
from .views import CreateAlbumClass, UpdateAlbumClass, DeleteAlbumClass

urlpatterns = [
    # path('', album, name='album'),
    path('', CreateAlbumClass.as_view(), name='album'),
    # path('<int:id>/edit/', edit_album, name='edit_album'),
    path('<int:id>/edit/', UpdateAlbumClass.as_view(), name='edit_album'),
    # path('<int:id>/delete/', delete_album, name='delete_album'),
    path('<int:id>/delete/', DeleteAlbumClass.as_view(), name='delete_album'),
]

