# Generated by Django 5.1.4 on 2025-02-03 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(default='static/images/default_avatar.png', upload_to='static/images/', verbose_name='Avatar'),
        ),
    ]
