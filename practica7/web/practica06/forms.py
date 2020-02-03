from django.forms import ModelForm
from .models import *

class GrupoForm(ModelForm):
  class Meta:
    model = Grupo
    fields = '__all__'

class MusicoForm(ModelForm):
  class Meta:
    model = Musico
    fields = '__all__'

class AlbumForm(ModelForm):
  class Meta:
    model = Album
    fields = '__all__'

