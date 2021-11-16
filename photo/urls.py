from django.urls import path

from . import views

urlpatterns = [
    path('album <str:pk_a>/photo <str:pk_p>/', views.one_photo, name='one_photo'),
    path('album <str:pk_a>/ajout_photo/', views.add_photo, name='add_photo'),
    path('album <str:pk_a>/modifier_photo <str:pk_p>/', views.update_photo, name='update_photo'),
    path('album <str:pk_a>/supprimer_photo <str:pk_p>/', views.delete_photo, name='delete_photo'),
]
