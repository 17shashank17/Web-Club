# Generated by Django 2.1.1 on 2019-08-23 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_remove_test_score_attempted'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_score',
            name='attempted',
            field=models.BooleanField(default=False),
        ),
    ]
