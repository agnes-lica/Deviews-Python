# Generated by Django 4.0.7 on 2023-01-10 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_alter_post_post_picture'),
        ('fires', '0007_remove_firepost_post_remove_firepost_user_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firepost',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fires', to='posts.post'),
        ),
        migrations.AddField(
            model_name='firepost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fires', to=settings.AUTH_USER_MODEL),
        ),
    ]
