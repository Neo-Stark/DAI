from django.db import models

class Grupo(models.Model):
  nombre = models.CharField(max_length=200)
  fecha_fundacion = models.DateField()
  estilo = models.CharField(max_length=200)

  def __str__(self):
    return self.nombre

class Musico(models.Model):
  grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE, null=True, blank=True)
  nombre = models.CharField(max_length=200)
  fecha_nacimiento = models.DateField(null=True)
  instrumento = models.CharField(max_length=200, null=True)
  # foto = models.ImageField( upload_to = 'static/img', null=True)

  def __str__(self):
    return self.nombre

class Album(models.Model):
  grupo = models.ForeignKey('Grupo', on_delete=models.CASCADE)
  titulo = models.CharField(max_length=200)
  fecha_lanzamiento = models.DateField(null=True)
  distribuidora = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.titulo