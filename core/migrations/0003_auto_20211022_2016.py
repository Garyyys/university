# Generated by Django 3.2.8 on 2021-10-22 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20211021_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='time_table',
        ),
        migrations.AddField(
            model_name='lecture',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.group'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lecture',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.teacher'),
        ),
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.group'),
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
    ]
