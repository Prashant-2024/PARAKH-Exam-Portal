# Generated by Django 4.2.5 on 2023-09-23 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_alter_quizcategory_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Level',
            },
        ),
    ]
