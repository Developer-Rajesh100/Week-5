from django.shortcuts import render
from musician.models import Musician
# from album.models import Album

# Create your views here.
def home(request):
    # musician_data = Musician.objects.all()
    musician_data = Musician.objects.prefetch_related('albums').all()
    # album_data = Album.objects.all()

    data = {
        'musician' : musician_data,
        # 'album' : album_data
    }

    return render(request, 'home.html', data)