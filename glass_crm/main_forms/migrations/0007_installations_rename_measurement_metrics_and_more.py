# Generated by Django 4.2.7 on 2023-11-12 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_forms', '0006_rename_customer_customers_customer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Installations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installation_date', models.DateField(verbose_name='Дата монтажа')),
                ('square_meters_count', models.CharField(max_length=255, verbose_name='Кол-во м2')),
                ('slopes', models.CharField(max_length=255, verbose_name='Откосы м/п')),
                ('price_per_square_meter', models.IntegerField(verbose_name='Стоимость м2')),
                ('additional_works', models.TextField(verbose_name='Доп. работы')),
                ('total_amount', models.IntegerField(verbose_name='Сумма')),
            ],
        ),
        migrations.RenameModel(
            old_name='Measurement',
            new_name='Metrics',
        ),
        migrations.DeleteModel(
            name='Installation',
        ),
        migrations.RenameField(
            model_name='metrics',
            old_name='measurement_date',
            new_name='metrics_date',
        ),
        migrations.AlterField(
            model_name='contracts',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='main_forms.customers'),
        ),
    ]