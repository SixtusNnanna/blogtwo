# Generated by Django 3.1.2 on 2020-12-09 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
