# Generated by Django 5.0 on 2023-12-07 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="city",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
