# Generated by Django 5.0.2 on 2024-03-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book66", "0005_order_customuser_orders"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
    ]
