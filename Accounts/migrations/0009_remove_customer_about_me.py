# Generated by Django 5.0.3 on 2024-03-30 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_remove_customer_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='about_me',
        ),
    ]