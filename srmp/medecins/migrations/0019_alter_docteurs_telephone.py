# Generated by Django 4.2.4 on 2023-09-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("medecins", "0018_remove_docteurs_anneesdepratique_docteurs_adresse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="docteurs",
            name="telephone",
            field=models.IntegerField(),
        ),
    ]