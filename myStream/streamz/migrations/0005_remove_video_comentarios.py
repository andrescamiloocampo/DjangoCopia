# Generated by Django 4.2.1 on 2023-05-12 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamz', '0004_alter_video_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='comentarios',
        ),
    ]
