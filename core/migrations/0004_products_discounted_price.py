# Generated by Django 4.2.4 on 2023-10-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_setting_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discounted_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]