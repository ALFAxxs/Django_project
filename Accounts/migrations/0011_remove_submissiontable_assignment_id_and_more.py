# Generated by Django 5.0.3 on 2024-03-31 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_rename_student_id_enrollmenttable_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissiontable',
            name='Assignment_ID',
        ),
        migrations.RemoveField(
            model_name='gradetable',
            name='submission_id',
        ),
        migrations.RemoveField(
            model_name='submissiontable',
            name='Student_id',
        ),
        migrations.DeleteModel(
            name='AssignmentTable',
        ),
        migrations.DeleteModel(
            name='GradeTable',
        ),
        migrations.DeleteModel(
            name='SubmissionTable',
        ),
    ]
