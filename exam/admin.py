from django.contrib import admin
# Register your models here.

from . import models

admin.site.register(models.QuizCategory)
admin.site.register(models.QuizLevel)
admin.site.register(models.QuizQuestion)