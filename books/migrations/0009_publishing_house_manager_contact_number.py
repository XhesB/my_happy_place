# Generated by Django 4.1.3 on 2022-11-09 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_delete_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishing_house',
            name='manager_contact_number',
            field=models.IntegerField(null=True),
        ),
    ]