# Generated by Django 3.1.7 on 2021-03-24 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(verbose_name='customer_id')),
                ('marketplace', models.TextField(verbose_name='marketplace')),
            ],
        ),
    ]
