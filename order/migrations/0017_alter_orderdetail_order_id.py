# Generated by Django 4.0.4 on 2022-06-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0016_alter_orderdetail_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]
