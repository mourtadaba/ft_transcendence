# Generated by Django 5.0.10 on 2025-01-31 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_last_played_game_profile_time_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='achievements',
            field=models.JSONField(default=list),
        ),
    ]
