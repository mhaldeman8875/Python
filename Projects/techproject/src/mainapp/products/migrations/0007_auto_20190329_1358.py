# Generated by Django 2.0.7 on 2019-03-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190329_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('drinks', 'drinks'), ('treats', 'treats'), ('entrees', 'entrees')], max_length=60),
        ),
    ]
