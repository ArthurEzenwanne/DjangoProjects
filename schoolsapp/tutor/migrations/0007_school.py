# Generated by Django 2.1.5 on 2019-01-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0006_auto_20190123_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('email_address', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('motto', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=1000)),
                ('slug', models.CharField(max_length=120, unique=True)),
                ('country', models.CharField(default='Nigeria', max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('town', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
    ]
