# Generated by Django 2.1.15 on 2020-05-20 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='like_usres',
            new_name='like_users',
        ),
    ]
