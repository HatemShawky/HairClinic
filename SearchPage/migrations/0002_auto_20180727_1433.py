# Generated by Django 2.0.7 on 2018-07-27 12:33

import SearchPage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='socialid',
            field=models.CharField(blank=True, max_length=14, unique=True, validators=[SearchPage.models.validate_14, SearchPage.models.validate_nostr]),
        ),
    ]
