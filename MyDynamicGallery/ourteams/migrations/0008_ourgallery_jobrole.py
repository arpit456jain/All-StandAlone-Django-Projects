# Generated by Django 3.1.3 on 2021-03-01 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourteams', '0007_delete_ourteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourgallery',
            name='jobrole',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
