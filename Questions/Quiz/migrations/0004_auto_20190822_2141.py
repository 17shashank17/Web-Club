# Generated by Django 2.1.1 on 2019-08-22 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_auto_20190822_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='answer_delete',
            new_name='relation',
        ),
        migrations.RenameField(
            model_name='questions',
            old_name='question_delete',
            new_name='relation',
        ),
        migrations.RenameField(
            model_name='user_info',
            old_name='user_delete',
            new_name='relation',
        ),
    ]