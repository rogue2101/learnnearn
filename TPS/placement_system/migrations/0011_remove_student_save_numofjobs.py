# Generated by Django 4.0.6 on 2022-08-29 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placement_system', '0010_student_save_numofjobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_save',
            name='numofjobs',
        ),
    ]