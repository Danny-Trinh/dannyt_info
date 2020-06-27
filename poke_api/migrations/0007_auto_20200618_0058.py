# Generated by Django 3.0.7 on 2020-06-18 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poke_api', '0006_auto_20200616_0551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='attack',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='b_attack',
            field=models.IntegerField(blank=True, verbose_name='base attack'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='b_defense',
            field=models.IntegerField(blank=True, verbose_name='base defense'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='b_hp',
            field=models.IntegerField(blank=True, verbose_name='base hp'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='b_s_attack',
            field=models.IntegerField(blank=True, verbose_name='base special attack'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='b_s_defense',
            field=models.IntegerField(blank=True, verbose_name='base special defense'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='b_speed',
            field=models.IntegerField(blank=True, verbose_name='base speed'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='defense',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='hp',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='s_attack',
            field=models.IntegerField(blank=True, verbose_name='special attack'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='s_defense',
            field=models.IntegerField(blank=True, verbose_name='special defense'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='speed',
            field=models.IntegerField(blank=True),
        ),
    ]