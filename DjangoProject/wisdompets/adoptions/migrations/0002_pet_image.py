# Generated by Django 2.2.4 on 2019-09-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='image',
            field=models.ImageField(blank=True, upload_to='pet_image'),
        ),
    ]
