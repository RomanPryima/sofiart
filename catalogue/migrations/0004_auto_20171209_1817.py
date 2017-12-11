# Generated by Django 2.0 on 2017-12-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20171209_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='articles',
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('published',)},
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to='articles/images'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]