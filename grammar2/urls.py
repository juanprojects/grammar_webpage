from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('<str:playerG2>/topic_explanation/', views.topic_explanationG2, name="topic_expG2"),
    path('<str:playerG2>/game_explanation/', views.game_explanationG2, name="game_expG2"),
    path('<str:playerG2>/exercise_1/', views.exercise_1, name="exercise_1"),
    path('<str:playerG2>/exercise_2/', views.exercise_2, name="exercise_2"),
    path('<str:playerG2>/exercise_3/', views.exercise_3, name="exercise_3"),
    path('<str:playerG2>/exercise_4/', views.exercise_4, name="exercise_4"),
    path('<str:playerG2>/exercise_5/', views.exercise_5, name="exercise_5"),
    path('<str:playerG2>/exercise_6/', views.exercise_6, name="exercise_6"),
    path('<str:playerG2>/exercise_7/', views.exercise_7, name="exercise_7"),
    path('<str:playerG2>/exercise_8/', views.exercise_8, name="exercise_8"),
    path('<str:playerG2>/exercise_9/', views.exercise_9, name="exercise_9"),
    path('<str:playerG2>/exercise_10/', views.exercise_10, name="exercise_10"),
    path('assign_score', views.assign_score, name="as_2"),
    path('<str:playerG2>/final_score/', views.final_score, name="final_score"),
]