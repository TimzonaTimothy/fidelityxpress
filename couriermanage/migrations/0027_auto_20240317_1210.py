# Generated by Django 3.0.5 on 2024-03-17 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0026_courier_sender_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courier',
            old_name='sender_phone',
            new_name='sender_phone_num',
        ),
    ]
