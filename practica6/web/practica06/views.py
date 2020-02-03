from django.shortcuts import render, HttpResponse, redirect
from .models import Musico
from .forms import *
from django.http import HttpResponseRedirect
import json


def index(request):
    return render(request, 'index.html')


def test_template(request):
    context = {'usuario': 'Ivan',
               }
    return render(request, 'test.html', context)


def render_form(request,class_form, url):
  if 'elemento' in request.POST:
    print(request.POST['elemento'])
  if request.method == 'POST':
    form = class_form(request.POST)

    if form.is_valid():
      form.save()
      return HttpResponseRedirect("/p6")
  else:
    form = class_form()

  return render(request, 'formulario_base.html', {'form': form, 'url': url})


def form_grupo(request):
  return render_form(request, GrupoForm, "/p6/grupos/form")

def form_album(request):
  return render_form(request, AlbumForm, "/p6/album/form")

def form_musico(request):
  return render_form(request, MusicoForm, "/p6/musicos/form")


def index(request):
  musicos = Musico.objects.all()
  grupos  = Grupo.objects.all()
  album  = Album.objects.all()

  return render(request, 'index.html', {'musicos':musicos, 'grupos':grupos, 'album':album})

def modificar(request, model, oid):
  switcher = {
    "Musico" : Musico,
    "Grupo" : Grupo,
    "Album" : Album
  }
  switcherForm = {
    "Musico" : MusicoForm,
    "Grupo" : GrupoForm,
    "Album" : AlbumForm
  }
  form = switcherForm.get(model)
  object = switcher.get(model).objects.filter(id=oid).first()
  if request.method == "POST":
      form = form(request.POST, instance=object)
      if form.is_valid():
        form.save()
        return redirect('index')
  else:
    form = form(instance=object)
  return render(request, 'formulario_base.html', {'form':form})

def eliminar(request, model, oid):
  switcher = {
    "Musico" : Musico,
    "Grupo" : Grupo,
    "Album" : Album
  }
  switcher.get(model).objects.filter(id=oid).delete()
  return redirect('index')