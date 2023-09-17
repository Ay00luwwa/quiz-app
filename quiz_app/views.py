from django.shortcuts import render
from .models import Question, Quiz
from django import forms

class Question(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'correct_answer']

def start_quiz(request, quiz_id):
    quiz = Quiz.objects.get(pk=quiz_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            # Handle form logic, save response, etc.
            return redirect('some-result-view')
    else:
        form = QuestionForm()
    return render(request, 'quiz_app/quiz.html', {'form': form, 'quiz': quiz})