# Generated by Django 5.1.2 on 2024-10-22 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_image_myuser_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='WorkArrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Full-Time', 'full-time'), ('Intern', 'intern'), ('Attachee', 'attachee')], max_length=50)),
                ('leave_balance', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'WorkArrangement',
                'verbose_name_plural': 'WorkArrangements',
            },
        ),
        migrations.AddField(
            model_name='myuser',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.department'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='arrangement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.workarrangement'),
        ),
    ]