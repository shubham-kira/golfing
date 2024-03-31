from django.urls import path
from . import views

urlpatterns = [
    path('', views.tournament_list, name='home_page'),
    path('tournament/<pk>/', views.tournament_detail, name='tournament_detail'),
    path('register/', views.reigster, name='register'),
    path('registration/<int:pk>/<int:user_id>/', views.register_a_player, name='register_a_player'),
    path('edit_score/<pk>/', views.edit_score, name='edit_score'),
    path('update_score/<pk>/', views.update_score, name='update_score')
]