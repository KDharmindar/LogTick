# Generated by Django 2.0 on 2017-12-30 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0007_projecttask_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttask',
            name='parent_task_id',
        ),
        migrations.AlterField(
            model_name='projecttask',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Project', to='Main.Project', verbose_name='Project'),
        ),
    ]
