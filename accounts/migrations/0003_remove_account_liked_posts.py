# Generated by Django 4.2 on 2023-04-21 07:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="liked_posts",
        ),
    ]
