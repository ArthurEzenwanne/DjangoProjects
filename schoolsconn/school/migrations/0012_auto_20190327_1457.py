# Generated by Django 2.1.7 on 2019-03-27 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20190327_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='nursery',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='primary',
            field=models.BooleanField(default=True),
        ),
    ]