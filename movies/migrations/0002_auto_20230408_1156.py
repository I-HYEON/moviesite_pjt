# Generated by Django 3.2.18 on 2023-04-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actor_image',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='movie',
            name='audience',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster_url',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_date',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='movie',
            name='score',
            field=models.FloatField(default=None),
        ),
    ]
