# Generated by Django 4.1.7 on 2023-09-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='area',
        ),
        migrations.AddField(
            model_name='customuser',
            name='areas',
            field=models.ManyToManyField(related_name='areas', to='authentication_service.area'),
        ),
    ]
