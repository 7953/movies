# Generated by Django 4.1.7 on 2024-02-02 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='image', upload_to='photo'),
            preserve_default=False,
        ),
    ]