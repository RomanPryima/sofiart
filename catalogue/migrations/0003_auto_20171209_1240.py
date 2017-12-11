# Generated by Django 2.0 on 2017-12-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20171209_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=45)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=None),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='name',
            field=models.TextField(max_length=45),
        ),
        migrations.AddField(
            model_name='image',
            name='articles',
            field=models.ManyToManyField(to='catalogue.Article'),
        ),
    ]