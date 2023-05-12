# Generated by Django 4.2.1 on 2023-05-12 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_orderpickup_orderitem_order_pickup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Orders.order'),
        ),
    ]
