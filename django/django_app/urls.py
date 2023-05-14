from django.urls import path
from .views import TeacherListView, TeacherScoreDetailView

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherScoreDetailView.as_view(), name='teacher_score_detail'),
]
