# Generated by Django 4.2.4 on 2023-10-08 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_products_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
