# Generated by Django 3.0.3 on 2020-03-16 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('comments', models.TextField()),
                ('news_id', models.IntegerField()),
                ('date', models.CharField(max_length=250)),
                ('time', models.CharField(max_length=250)),
            ],
        ),
    ]
