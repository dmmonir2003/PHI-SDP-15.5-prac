from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.

def add_musician(request):
    if request.method=='POST':
        musician_form=forms.MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('add_musician')
    else:
         musician_form=forms.MusicianForm()
    return render(request,'add_musician.html',{'forms':musician_form})

class AddMusicianView(CreateView):
      model=models.MusicianModel
      form_class=forms.MusicianForm
      template_name='add_musician.html'
      success_url=reverse_lazy('add_musician')
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context["forms"] =context['form']
          return context
      
    


def edit_musician(request,id):
    musician=models.MusicianModel.objects.get(pk=id)
    musician_form=forms.MusicianForm(instance=musician)
    if request.method=='POST':
        musician_form=forms.MusicianForm(request.POST,instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    
    return render(request,'add_musician.html',{'forms':musician_form})


class EditMusician(UpdateView):
      model=models.MusicianModel
      form_class=forms.MusicianForm
      template_name='add_musician.html'
      success_url=reverse_lazy('homepage')
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          context["forms"] = context['form']
          return context
      

