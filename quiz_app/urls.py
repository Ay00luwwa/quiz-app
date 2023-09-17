from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),       # To display a list of available quizzes
    path('quiz/<int:quiz_id>/', views.start_quiz, name='start_quiz'), # To start a specific quiz
    # ... add other paths as needed
]
