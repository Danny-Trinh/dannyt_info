# Generated by Django 3.0.7 on 2020-06-18 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke_api', '0012_auto_20200618_0119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pokemon',
            name='base_refreshed',
        ),
        migrations.AddField(
            model_name='pokemon',
            name='number',
            field=models.CharField(default=3, editable=False, max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(default=models.CharField(default='venusaur', max_length=30), max_length=30),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='species',
            field=models.CharField(default='venusaur', max_length=30),
        ),
    ]
