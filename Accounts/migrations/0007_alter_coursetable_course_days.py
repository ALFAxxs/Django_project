# Generated by Django 5.0.3 on 2024-03-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_alter_coursetable_course_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetable',
            name='Course_Days',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Free', 'Free')], max_length=20),
        ),
    ]
