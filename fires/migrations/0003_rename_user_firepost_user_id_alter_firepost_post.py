# Generated by Django 4.0.7 on 2023-01-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fires', '0002_alter_firepost_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firepost',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='firepost',
            name='post',
            field=models.IntegerField(),
        ),
    ]