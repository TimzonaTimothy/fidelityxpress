# Generated by Django 3.0.5 on 2023-12-05 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriermanage', '0024_auto_20230619_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='sender_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='courier',
            name='sender_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]