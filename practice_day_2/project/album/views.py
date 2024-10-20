from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import AlbumForm
from .models import Album

# Create your views here.
# def album(request):
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#             return redirect('home')
#     else:
#         form = AlbumForm()
#     return render(request, 'album.html', {'form': form})


class CreateAlbumClass(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('home')



# def edit_album(request, id):
#     alb = Album.objects.get(pk = id)
#     alb_form = AlbumForm(instance = alb)
#     if request.method == 'POST':
#         alb_form = AlbumForm(request.POST, instance = alb)
#         if alb_form.is_valid():
#             alb_form.save()
#             return redirect('home')
#     return render(request, 'album.html', {'form': alb_form})


class UpdateAlbumClass(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


# def delete_album(request, id):
#     alb = Album.objects.get(pk=id)
#     alb.delete()
#     return redirect('home')


class DeleteAlbumClass(DeleteView):
    model = Album
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')