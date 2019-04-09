# Generated by Django 2.1.7 on 2019-04-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20190407_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentMultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_multiple', models.CharField(blank=True, max_length=255)),
                ('doc_multiple', models.FileField(blank=True, upload_to='schools/multiple/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='document',
            name='desc_multiple',
        ),
        migrations.RemoveField(
            model_name='document',
            name='doc_multiple',
        ),
    ]