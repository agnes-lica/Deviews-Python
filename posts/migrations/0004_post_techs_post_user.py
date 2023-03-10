# Generated by Django 4.0.7 on 2023-01-10 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('techs', '0005_alter_tech_tech_name'),
        ('posts', '0003_alter_post_post_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='techs',
            field=models.ManyToManyField(related_name='posts', to='techs.tech'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
