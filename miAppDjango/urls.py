from django.urls import path
from . import views

urlpatterns = [
    path('person', views.index, name='index'),
    path('car', views.index, name='index2'),
    path('persona/<int:persona_id>/', views.detail, name='detail'),
    path('carro/<int:carro_id>/', views.detail2, name='detail2'),
]