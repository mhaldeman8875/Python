# Generated by Django 2.0.7 on 2019-03-29 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20190329_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treats', 'treats'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('appetizers', 'appetizers')], max_length=60),
        ),
    ]
