# Generated by Django 4.0.2 on 2022-02-15 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_cart', '0003_alter_movie_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='description',
            new_name='desc',
        ),
    ]
