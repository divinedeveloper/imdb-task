# Generated by Django 3.0.7 on 2020-07-30 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popularity', models.FloatField()),
                ('director', models.CharField(max_length=200)),
                ('imdb_score', models.FloatField()),
                ('name', models.CharField(max_length=200)),
                ('genre', models.ManyToManyField(to='api.Genre')),
            ],
        ),
    ]
