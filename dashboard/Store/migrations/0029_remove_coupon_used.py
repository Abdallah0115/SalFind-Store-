# Generated by Django 4.2.5 on 2024-04-16 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0028_coupon_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='used',
        ),
    ]