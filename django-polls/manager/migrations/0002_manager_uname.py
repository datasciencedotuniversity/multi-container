# Generated by Django 3.0.3 on 2020-03-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='uname',
            field=models.CharField(default='', max_length=250),
        ),
    ]
