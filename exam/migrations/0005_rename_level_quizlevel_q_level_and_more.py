# Generated by Django 4.2.5 on 2023-09-23 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_quizlevel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizlevel',
            old_name='level',
            new_name='q_level',
        ),
        migrations.AlterField(
            model_name='quizquestion',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_set', to='exam.quizcategory'),
        ),
    ]