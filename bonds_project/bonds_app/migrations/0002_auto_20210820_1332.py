# Generated by Django 3.2.6 on 2021-08-20 19:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bonds_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bond',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bond',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
