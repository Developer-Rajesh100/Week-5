from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import MusicianForm
from .models import Musician

# Create your views here.
# def musician(request):
#     if request.method == 'POST':
#         form = MusicianForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data)
#             return redirect('musician')
#     else:
#         form = MusicianForm()
#     return render(request, 'musician.html', {'form': form})


# Add Musician using Class based view
class AddMusicianClass(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('home')



# def edit_musician(request, id):
#     mus = Musician.objects.get(pk = id)
#     mus_form = MusicianForm(instance = mus)
#     if request.method == 'POST':
#         mus_form = MusicianForm(request.POST, instance = mus)
#         if mus_form.is_valid():
#             mus_form.save()
#             redirect('home')
#     return render(request, 'musician.html', {'form': mus_form})


# Update Musician Class
class editMusicianClass(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')