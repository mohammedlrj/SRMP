# Generated by Django 4.2 on 2023-09-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medecins', '0024_alter_docteurs_telephone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docteurs',
            name='fullname',
            field=models.CharField(default='', max_length=50),
        ),
    ]