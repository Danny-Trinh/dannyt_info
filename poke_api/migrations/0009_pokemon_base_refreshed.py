# Generated by Django 3.0.7 on 2020-06-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke_api', '0008_auto_20200618_0104'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='base_refreshed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
