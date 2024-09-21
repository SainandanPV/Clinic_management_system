# Generated by Django 5.0.7 on 2024-09-21 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="patientdata",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("age", models.IntegerField(null=True)),
                ("lastvisit", models.DateField(auto_now=True)),
                ("data", models.TextField(blank=True, null=True)),
            ],
        ),
    ]