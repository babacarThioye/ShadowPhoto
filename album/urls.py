from django.urls import path

from . import views

urlpatterns = [
    path('album <str:pk_a>/', views.one_album, name='one_album'),
    path('ajout <str:pk_u>/', views.add_album, name='add_album'),

]
