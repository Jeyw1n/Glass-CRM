# Generated by Django 4.2.6 on 2023-10-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contracts",
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
                ("contract_number", models.IntegerField()),
                ("address", models.TextField()),
                ("customer", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=255)),
                ("price", models.IntegerField()),
                ("prepayment", models.IntegerField()),
                ("debt", models.IntegerField()),
                ("delivery_date", models.DateField()),
                ("montage_date", models.DateField()),
                ("delivery_date_by_contract", models.DateField()),
            ],
        ),
    ]