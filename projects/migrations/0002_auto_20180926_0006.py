# Generated by Django 2.1.1 on 2018-09-26 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='proyecto/'),
        ),
    ]
