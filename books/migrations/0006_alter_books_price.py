# Generated by Django 4.1.3 on 2022-11-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_client_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]