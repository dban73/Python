from django.urls import path, include
from django.urls.conf import include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('personas',views.PersonaViewSet)

urlpatterns = [
    path('', views.index, name='index'),
  #  path('car', views.index, name='index2'),
    path('persona/<int:persona_id>/', views.detail, name='detail'),
   # path('carro/<int:carro_id>/', views.detail2, name='detail2'),
    path('api/', include(router.urls)),
]