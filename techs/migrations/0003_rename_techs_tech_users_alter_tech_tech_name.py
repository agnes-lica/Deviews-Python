# Generated by Django 4.0.7 on 2023-01-09 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techs', '0002_alter_tech_options_tech_tech_name_tech_techs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tech',
            old_name='techs',
            new_name='users',
        ),
        migrations.AlterField(
            model_name='tech',
            name='tech_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
