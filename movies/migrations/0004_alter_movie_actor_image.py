# Generated by Django 3.2.18 on 2023-04-08 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_actor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
