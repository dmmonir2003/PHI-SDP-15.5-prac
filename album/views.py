from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.views.generic import CreateView,UpdateView
# Create your views here.

def add_album(request):
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
         album_form=forms.AlbumForm()
    return render(request,'add_album.html',{'forms':album_form})

class AddAlbumView(CreateView):
    model=models.AlbumModel
    template_name='add_album.html'
    form_class=forms.AlbumForm
    success_url=reverse_lazy('add_album')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = context['form']
        return context
    


def edit_album(request,id):
    album=models.AlbumModel.objects.get(pk=id)
    album_form=forms.AlbumForm(instance=album)
    if request.method=='POST':
        album_form=forms.AlbumForm(request.POST,instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    return render(request,'add_album.html',{'forms':album_form})


class EditAlbumView(UpdateView):
    pass


def delete_album(request,id):
    album=models.AlbumModel.objects.get(pk=id)
    album.delete()
    return redirect('homepage')