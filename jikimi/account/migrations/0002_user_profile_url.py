# Generated by Django 4.1.1 on 2023-02-08 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_url",
            field=models.ImageField(blank=True, null=True, upload_to="profile_img/"),
        ),
    ]