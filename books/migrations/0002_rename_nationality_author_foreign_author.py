# Generated by Django 4.1.3 on 2022-11-07 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='nationality',
            new_name='foreign_author',
        ),
    ]
