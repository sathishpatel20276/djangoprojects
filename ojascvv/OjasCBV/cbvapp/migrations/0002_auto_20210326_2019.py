# Generated by Django 3.1.7 on 2021-03-26 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]