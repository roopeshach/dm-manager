# Generated by Django 4.1 on 2022-08-21 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0005_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10, null=True),
        ),
    ]