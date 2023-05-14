from django.db import models


class Teachers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Teams(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SeniorQuestions(models.Model):
    
    question_a_1 = models.IntegerField()
    question_a_2 = models.IntegerField()
    question_a_3 = models.IntegerField()
    question_a_4 = models.IntegerField()
    question_a_5 = models.IntegerField()
    question_b_1 = models.IntegerField()
    question_c_1 = models.IntegerField()
    question_c_2 = models.IntegerField()
    question_d_1 = models.IntegerField()
    question_d_2 = models.IntegerField()
    question_e_1 = models.IntegerField()
    question_e_2 = models.IntegerField()
    teacher = models.ForeignKey('Teachers', on_delete=models.CASCADE)
    team = models.ForeignKey('Teams', on_delete=models.CASCADE)
