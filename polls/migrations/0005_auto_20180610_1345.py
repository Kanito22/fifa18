# Generated by Django 2.0.5 on 2018-06-10 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180610_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='id',
        ),
        migrations.AlterField(
            model_name='score',
            name='choice',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='polls.Choice'),
        ),
    ]
