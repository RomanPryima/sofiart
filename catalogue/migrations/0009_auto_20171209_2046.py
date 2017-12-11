# Generated by Django 2.0 on 2017-12-09 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20171209_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL),
        ),
    ]