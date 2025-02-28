# Generated by Django 5.1.4 on 2025-02-17 01:04

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_message_is_game_invite_alter_message_timestamp_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gameinvite',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='gameinvite',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Declined')], default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterUniqueTogether(
            name='gameinvite',
            unique_together={('sender', 'recipient', 'status', 'timestamp')},
        ),
    ]
