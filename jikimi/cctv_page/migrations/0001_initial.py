# Generated by Django 4.1.1 on 2023-01-26 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                ("region_id", models.AutoField(primary_key=True, serialize=False)),
                ("region_si", models.CharField(max_length=20)),
                ("region_gu", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "Region",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="School",
            fields=[
                ("school_id", models.AutoField(primary_key=True, serialize=False)),
                ("school_name", models.CharField(max_length=30)),
                ("school_address2", models.CharField(max_length=100, unique=True)),
                (
                    "school_phone",
                    models.CharField(blank=True, max_length=11, null=True, unique=True),
                ),
                ("school_type", models.CharField(max_length=30)),
                ("school_agency", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "School",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="SchoolData",
            fields=[
                ("school_data_id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "school_studentnum",
                    models.IntegerField(
                        blank=True, db_column="school_studentNum", null=True
                    ),
                ),
                (
                    "school_yearlybullying",
                    models.IntegerField(
                        blank=True, db_column="school_yearlyBullying", null=True
                    ),
                ),
                (
                    "school_data_risk",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
            ],
            options={
                "db_table": "School_data",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_id",
                    models.CharField(max_length=30, primary_key=True, serialize=False),
                ),
                ("user_passwd", models.CharField(max_length=30)),
                ("user_email", models.CharField(max_length=60, unique=True)),
                (
                    "user_phone",
                    models.CharField(blank=True, max_length=11, null=True, unique=True),
                ),
            ],
            options={
                "db_table": "User",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                ("video_id", models.AutoField(primary_key=True, serialize=False)),
                ("video_date", models.DateField()),
                ("video_start_time", models.TimeField()),
                ("video_end_time", models.TimeField()),
                ("video_path", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "video_isviolence",
                    models.CharField(
                        blank=True,
                        db_column="video_isViolence",
                        max_length=50,
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "Video",
                "managed": False,
            },
        ),
    ]
