# Generated by Django 2.1.7 on 2019-02-27 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicSchoolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motto', models.CharField(blank=True, default='N/A', max_length=256, null=True)),
                ('description', models.CharField(blank=True, default='No description yet...', max_length=1000, null=True)),
                ('country', models.CharField(default='Nigeria', max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('lga', models.CharField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('town', models.CharField(blank=True, max_length=50, null=True)),
                ('street', models.CharField(max_length=640)),
                ('approval_number', models.CharField(default='Awaiting', max_length=11)),
                ('admin', models.CharField(default='N/A', max_length=128)),
                ('school_type', models.CharField(choices=[('c', 'Creche'), ('np', 'Nursery-Primary'), ('s', 'Secondary'), ('al', 'A-Levels')], default='np', max_length=2)),
                ('approved_exams', models.CharField(choices=[('ncce', 'National Common Entrance Examinations'), ('scce', 'State Common Entrance Examinatins'), ('waec', 'West African Examination Council Exams'), ('neco', 'National Examinations Council Exams'), ('jwaec', 'Junior West African Examination Council Exams'), ('jneco', 'Junior National Examinations Council Exams'), ('toefl', 'TOEFL Exams'), ('ielts', 'IELTS Exams'), ('alevel', 'A-Levels Exams'), ('igcse', 'IGCSE Exams')], default='ncce', max_length=6)),
                ('gender', models.CharField(choices=[('m', 'Male Only'), ('f', 'Female Only'), ('mx', 'Mixed')], default='mixed', max_length=6)),
                ('boarding', models.CharField(choices=[('fb', 'Full Boarding'), ('fd', 'Day Only'), ('bd', 'Day and Boarding')], default='bd', max_length=2)),
                ('founded', models.DateField(default='N/A')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=15)),
                ('slug', models.SlugField(max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='country',
            field=models.CharField(default='Nigeria', max_length=20),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='fname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='lga',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='lname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='schools',
            field=models.SmallIntegerField(blank=True, default=0, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='state',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='street',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='schoolsconnbaseuser',
            name='town',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='schoolsconnbaseuser',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='basicschoolinfo',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.School'),
        ),
    ]