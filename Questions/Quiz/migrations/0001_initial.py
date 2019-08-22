# Generated by Django 2.1.1 on 2019-08-22 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiser', models.CharField(default='', max_length=15)),
                ('name_quiz', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='question_delete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quiz.Quiz'),
        ),
    ]
