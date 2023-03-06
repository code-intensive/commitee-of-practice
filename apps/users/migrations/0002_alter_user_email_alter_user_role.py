# Generated by Django 4.1.5 on 2023-02-09 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                db_index=True, max_length=254, unique=True, verbose_name="email address"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "admin"),
                    ("mentor", "mentor"),
                    ("mentee", "mentee"),
                    ("consortium_member", "consortium_member"),
                ],
                db_index=True,
                default="mentee",
                max_length=20,
                verbose_name="role",
            ),
        ),
    ]