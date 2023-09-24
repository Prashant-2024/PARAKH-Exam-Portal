from django.db import models

# Create your models here.

class QuizCategory(models.Model):
    title=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title

class QuizLevel(models.Model):
    level=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Levels'

    def __str__(self):
        return self.level


class QuizQuestion(models.Model):
    category=models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    level=models.ForeignKey(QuizLevel, on_delete=models.CASCADE)
    question=models.TextField()
    opt1=models.CharField(max_length=500)
    opt2=models.CharField(max_length=500)
    opt3=models.CharField(max_length=500)
    opt4=models.CharField(max_length=500)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='Questions'

    def __str__(self):
        return self.question