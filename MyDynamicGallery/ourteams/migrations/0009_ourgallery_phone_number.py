# Generated by Django 3.1.3 on 2021-03-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteams', '0008_ourgallery_jobrole'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourgallery',
            name='phone_number',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
