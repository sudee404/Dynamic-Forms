# Generated by Django 5.1.2 on 2024-10-22 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_department_workarrangement_myuser_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='arrangement',
            field=models.CharField(choices=[('Full-Time', 'full-time'), ('Intern', 'intern'), ('Attachee', 'attachee')], default='Full-Time', max_length=50),
        ),
        migrations.DeleteModel(
            name='WorkArrangement',
        ),
    ]
