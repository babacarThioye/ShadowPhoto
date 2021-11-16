from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('utilisateur <str:pk>/', views.one_user, name='one_user'),
    path('ajout_utilisateur/', views.add_user, name='add_user'),
    path('A Propos /', views.a_propos, name='a_propos'),
]
