# Generated by Django 3.0.6 on 2020-06-04 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_forumpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('res', models.FileField(default='resume.pdf', upload_to='resume')),
            ],
        ),
    ]
