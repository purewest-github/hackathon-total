from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Score(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.question.title}: {self.score}"
