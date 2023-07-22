# Generated by Django 4.2.3 on 2023-07-20 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DemoApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.CharField(max_length=15)),
                ('ename', models.CharField(max_length=30)),
                ('edesn', models.CharField(choices=[('0', 'Select Your Designation '), ('1', 'Junior Trainee'), ('2', 'Senior Trainee'), ('3', 'Manager ')], default='0', max_length=20)),
                ('eexprev', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
