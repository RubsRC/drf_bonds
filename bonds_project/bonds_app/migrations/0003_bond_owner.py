# Generated by Django 3.2.6 on 2021-08-22 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bonds_app', '0002_auto_20210820_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='bond',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bonds', to='auth.user'),
            preserve_default=False,
        ),
    ]
