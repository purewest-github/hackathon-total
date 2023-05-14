from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Sum
from .models import Teachers, Teams, SeniorQuestions
from django.urls import reverse
from .forms import ScoreForm

# Create your views here.
class TeacherListView(ListView):
    model = Teachers
    template_name = 'teacher_list.html'  # 適切なテンプレート名に変更してください
    context_object_name = 'teachers'


