# Generated by Django 4.0.4 on 2022-05-08 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
