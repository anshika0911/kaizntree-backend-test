# Generated by Django 4.1.13 on 2024-02-11 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Items",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sku", models.CharField(max_length=100)),
                ("category_id", models.IntegerField()),
                ("in_stock", models.IntegerField()),
                ("available_stock", models.IntegerField()),
            ],
        ),
    ]
