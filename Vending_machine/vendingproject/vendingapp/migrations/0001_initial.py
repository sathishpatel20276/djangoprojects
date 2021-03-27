# Generated by Django 3.1.7 on 2021-03-26 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vending_machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cooldrink_name', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, default=False, max_digits=10)),
            ],
        ),
    ]
