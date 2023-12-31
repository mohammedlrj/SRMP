# Generated by Django 4.2 on 2023-09-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medecins", "0021_remove_docteurs_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="DocteurSignUp",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_login", models.DateTimeField(auto_now=True)),
                ("fullname", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=254)),
                ("password1", models.CharField(default="", max_length=128)),
                ("password2", models.CharField(default="", max_length=128)),
            ],
        ),
    ]
