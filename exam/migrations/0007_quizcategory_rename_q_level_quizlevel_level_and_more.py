# Generated by Django 4.2.5 on 2023-09-23 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0006_remove_quizquestion_category_delete_quizcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('detail', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RenameField(
            model_name='quizlevel',
            old_name='q_level',
            new_name='level',
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_set', to='exam.quizcategory'),
        ),
    ]
