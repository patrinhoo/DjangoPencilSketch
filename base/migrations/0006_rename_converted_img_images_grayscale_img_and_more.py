# Generated by Django 4.0.3 on 2022-03-26 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_images_converted_size_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='images',
            old_name='converted_img',
            new_name='grayscale_img',
        ),
        migrations.AddField(
            model_name='images',
            name='sketch_img',
            field=models.ImageField(null=True, upload_to='sketch/'),
        ),
    ]
