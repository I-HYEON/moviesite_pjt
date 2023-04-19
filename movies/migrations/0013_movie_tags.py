# Generated by Django 3.2.18 on 2023-04-16 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(related_name='movies', to='movies.Tag'),
        ),
    ]
