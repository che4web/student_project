# Generated by Django 3.1.2 on 2020-11-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_auto_20201119_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='studentapp.Course'),
        ),
    ]
