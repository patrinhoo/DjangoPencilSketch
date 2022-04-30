# Generated by Django 4.0.3 on 2022-03-25 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AddField(
            model_name='image',
            name='sketch',
            field=models.ImageField(default=0, upload_to='sketches'),
            preserve_default=False,
        ),
    ]
