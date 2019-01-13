# Generated by Django 2.0 on 2019-01-13 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20190113_1103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parent',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='parent',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='gender',
            field=models.CharField(choices=[('f', 'Female'), ('m', 'Male')], default='f', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parent',
            name='last_name',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Address',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Phone',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2019, 1, 13, 12, 23, 22, 146724)),
            preserve_default=False,
        ),
    ]