# Generated by Django 3.1.3 on 2021-03-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteams', '0012_auto_20210301_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourgallery',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=13),
        ),
    ]