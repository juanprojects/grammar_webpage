from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<str:player>/topic_explanation/', views.topic_explanation, name="topic_exp"),
    path('<str:player>/game_explanation/', views.game_explanation, name="game_exp"),
    path('<str:player>/nominal_group_1/', views.nominal_group_1, name="nominal_group_1"),
    path('<str:player>/nominal_group_2/', views.nominal_group_2, name="nominal_group_2"),
    path('<str:player>/nominal_group_3/', views.nominal_group_3, name="nominal_group_3"),
    path('<str:player>/nominal_group_4/', views.nominal_group_4, name="nominal_group_4"),
    path('<str:player>/nominal_group_5/', views.nominal_group_5, name="nominal_group_5"),
    path('<str:player>/nominal_group_6/', views.nominal_group_6, name="nominal_group_6"),
    path('<str:player>/nominal_group_7/', views.nominal_group_7, name="nominal_group_7"),
    path('assign_score', views.assign_score, name="as"),
    path('<str:player>/final_score/', views.final_score, name="final_score"),
]