# Generated by Django 3.0.5 on 2023-06-19 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0023_auto_20230428_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='reference',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='details',
        ),
    ]