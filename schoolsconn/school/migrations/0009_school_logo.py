# Generated by Django 2.1.7 on 2019-04-08 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20190408_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='logo',
            field=models.ImageField(blank=True, upload_to='<django.db.models.fields.SlugField>/logo/'),
        ),
    ]
