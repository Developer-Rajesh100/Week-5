from django.urls import path
from .views import AddMusicianClass, editMusicianClass

urlpatterns = [
    # path('', musician, name='musician'),
    path('', AddMusicianClass.as_view(), name='musician'),
    # path('<int:id>', edit_musician, name = 'edit_musician'),
    path('<int:id>', editMusicianClass.as_view(), name = 'edit_musician')
]
