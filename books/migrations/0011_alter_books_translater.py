# Generated by Django 4.1.3 on 2022-11-09 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_publishing_house_manager_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='translater',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.translater'),
        ),
    ]