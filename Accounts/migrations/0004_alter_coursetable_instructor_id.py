# Generated by Django 5.0.3 on 2024-03-27 09:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_alter_customer_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetable',
            name='Instructor_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
