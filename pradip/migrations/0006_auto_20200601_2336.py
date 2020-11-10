# Generated by Django 3.0.6 on 2020-06-01 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pradip', '0005_auto_20200601_2335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='album',
        ),
        migrations.AddField(
            model_name='gallery',
            name='gname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_gallery', to='pradip.Album'),
        ),
    ]