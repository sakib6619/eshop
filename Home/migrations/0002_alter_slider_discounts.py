# Generated by Django 4.2.6 on 2023-10-16 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='Discounts',
            field=models.IntegerField(),
        ),
    ]
