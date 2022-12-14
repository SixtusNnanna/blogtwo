# Generated by Django 3.1.2 on 2020-11-05 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201026_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
