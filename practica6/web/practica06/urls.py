
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
# from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register('grupo',views.GrupoViewSet)
# router.register('musico',views.MusicoViewSet)
# router.register('album',views.AlbumViewSet)

urlpatterns = [
    # path('form_genero'),
    url(r'^grupos/form', views.form_grupo, name='form_grupo'),
    url(r'^album/form', views.form_album, name='form_album'),
    url(r'^musicos/form', views.form_musico, name='form_musico'),
    url(r'^$', views.index, name='index'),
    url(r'^modificar/(?P<model>\w+)/(?P<oid>[0-9]+)/$', views.modificar, name='modificar'),
    url(r'^eliminar/(?P<model>\w+)/(?P<oid>[0-9]+)/$', views.eliminar, name='eliminar'),
]
