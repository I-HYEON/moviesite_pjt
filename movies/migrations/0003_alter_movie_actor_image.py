# Generated by Django 3.2.18 on 2023-04-08 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20230408_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]