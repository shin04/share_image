# Generated by Django 2.2 on 2019-06-25 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]
