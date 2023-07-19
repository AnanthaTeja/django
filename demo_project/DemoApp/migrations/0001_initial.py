# Generated by Django 3.0 on 2023-07-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("roll", models.CharField(max_length=15)),
                ("sname", models.CharField(max_length=30)),
                ("year", models.IntegerField()),
                ("branch", models.CharField(max_length=30)),
            ],
        ),
    ]
