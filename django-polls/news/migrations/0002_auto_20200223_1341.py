# Generated by Django 3.0.3 on 2020-02-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='catid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='catname',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='news',
            name='show',
            field=models.IntegerField(default=0),
        ),
    ]
