# Generated by Django 5.0.4 on 2024-04-09 11:02

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("supplier", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="suppliers",
            new_name="Member",
        ),
    ]
