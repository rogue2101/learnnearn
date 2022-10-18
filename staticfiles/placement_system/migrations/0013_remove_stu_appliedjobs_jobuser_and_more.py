# Generated by Django 4.0.6 on 2022-08-29 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placement_system', '0012_stu_appliedjobs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stu_appliedjobs',
            name='jobuser',
        ),
        migrations.RemoveField(
            model_name='stu_appliedjobs',
            name='user',
        ),
        migrations.AddField(
            model_name='stu_appliedjobs',
            name='collage_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='placement_system.student_save'),
        ),
        migrations.AddField(
            model_name='stu_appliedjobs',
            name='jccode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]