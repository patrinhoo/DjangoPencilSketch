# Generated by Django 4.0.3 on 2022-03-26 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_rename_converted_img_images_grayscale_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='grayscale_img',
            field=models.ImageField(null=True, upload_to='grayscale/'),
        ),
    ]
