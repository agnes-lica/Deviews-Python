# Generated by Django 4.0.7 on 2023-01-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techs', '0004_remove_tech_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech',
            name='tech_name',
            field=models.CharField(max_length=100),
        ),
    ]
