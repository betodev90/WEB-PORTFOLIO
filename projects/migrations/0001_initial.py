# Generated by Django 2.1.1 on 2018-09-25 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Este campo es referente al titulo del proyecto', max_length=120, verbose_name='Title')),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='proyecto/')),
                ('url', models.URLField()),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
