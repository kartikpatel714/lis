# Generated by Django 4.1.2 on 2023-01-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratoryapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_category',
            name='l_name',
            field=models.CharField(default='', max_length=200, verbose_name='Lab Name'),
        ),
    ]
