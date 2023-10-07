# Generated by Django 4.2.4 on 2023-08-21 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("patient", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="sexe",
            field=models.CharField(
                choices=[("H", "Homme"), ("F", "Femme")],
                default=django.utils.timezone.now,
                max_length=1,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="telephone",
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="patient",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]