from django.contrib import admin

from . import models

admin.site.register(models.Grupo)
admin.site.register(models.Musico)
admin.site.register(models.Album)