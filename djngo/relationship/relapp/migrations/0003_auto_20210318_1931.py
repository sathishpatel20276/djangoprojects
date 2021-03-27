# Generated by Django 3.1.7 on 2021-03-18 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relapp', '0002_auto_20210318_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_name', models.CharField(max_length=100)),
                ('actor_rating', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_name', models.CharField(max_length=50)),
                ('m_theatre', models.CharField(max_length=100)),
                ('ticket_price', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='bankaccount',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
        migrations.AddField(
            model_name='actor',
            name='movie',
            field=models.ManyToManyField(to='relapp.movie'),
        ),
    ]