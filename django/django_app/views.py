from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.db.models import Sum
from .models import Teacher, Score, Team
from django.urls import reverse
from .forms import ScoreForm

# Create your views here.
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'  # 適切なテンプレート名に変更してください
    context_object_name = 'teachers'


# class TeacherScoreDetailView(DetailView):
#     model = Teacher
#     template_name = 'teacher_score_detail.html'  # 適切なテンプレート名に変更してください
#     context_object_name = 'teacher'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         teacher = self.get_object()

#         teams = Team.objects.all()
#         for team in teams:
#             team_scores = Score.objects.filter(teacher=teacher, team=team)
#             team.total_score = team_scores.aggregate(Sum('score'))['score__sum'] or 0

#         context['teams'] = teams
#         return context

# class TeacherScoreDetailView(DetailView):
#     model = Teacher
#     template_name = 'teacher_score_detail.html'  # 適切なテンプレート名に変更してください
#     context_object_name = 'teacher'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         teacher = self.get_object()

#         teams = Team.objects.all()
#         for team in teams:
#             team_scores = Score.objects.filter(teacher=teacher, team=team)
#             team.total_score = team_scores.aggregate(Sum('score'))['score__sum'] or 0
#             team.scores = team_scores

#         context['teams'] = teams
#         return context



class TeacherScoreDetailView(DetailView):
    model = Teacher
    template_name = 'teacher_score_detail.html'  # 適切なテンプレート名に変更してください
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teacher = self.get_object()

        teams = Team.objects.all()
        for team in teams:
            team_scores = Score.objects.filter(teacher=teacher, team=team)
            team.total_score = team_scores.aggregate(Sum('score'))['score__sum'] or 0
            team.scores = [{'question': s.question, 'score': s.score, 'form': ScoreForm(instance=s)} for s in team_scores]

        context['teams'] = teams
        return context

    def post(self, request, *args, **kwargs):
        form = ScoreForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse('teacher_score_detail', args=[self.get_object().id]))
