# Generated by Django 2.0.5 on 2018-06-29 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20180610_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]