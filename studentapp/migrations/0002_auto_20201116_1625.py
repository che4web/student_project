# Generated by Django 3.1.2 on 2020-11-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proffessor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('age', models.IntegerField(blank=True, null=True, verbose_name='ФИО')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
    ]
