from django.urls import path
from . import views

urlpatterns = [
    path('times/', views.time_list, name='time_list'),
    path('times/create/', views.time_create, name='time_create'),
    path('times/update/<int:id>/', views.time_update, name='time_update'),
    path('times/delete/<int:id>/', views.time_delete, name='time_delete'),

    path('jogadores/', views.jogador_list, name='jogador_list'),
    path('jogadores/create/', views.jogador_create, name='jogador_create'),
    path('jogadores/update/<int:id>/', views.jogador_update, name='jogador_update'),
    path('jogadores/delete/<int:id>/', views.jogador_delete, name='jogador_delete'),
]
