# Generated by Django 5.0.2 on 2024-03-07 06:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("book66", "0002_alter_customuser_options_alter_customuser_managers_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_type",
            field=models.CharField(
                choices=[("admin", "Admin"), ("buyer", "Buyer"), ("seller", "Seller")],
                default="buyer",
                max_length=10,
            ),
        ),
    ]
