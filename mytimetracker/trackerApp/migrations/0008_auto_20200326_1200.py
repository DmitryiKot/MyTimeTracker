# Generated by Django 3.0.4 on 2020-03-26 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackerApp', '0007_highleveltask_finish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highleveltask',
            name='finish_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 1, 0, 0)),
        ),
    ]
