# Generated by Django 3.1.2 on 2020-12-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0007_auto_20201203_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]