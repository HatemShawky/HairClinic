# Generated by Django 2.1 on 2018-08-08 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SearchPage', '0003_aalopecia_aareata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aalopecia',
            name='sinlair',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='aareata',
            name='salt',
            field=models.IntegerField(),
        ),
    ]
