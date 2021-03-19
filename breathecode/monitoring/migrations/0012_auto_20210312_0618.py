# Generated by Django 3.1.7 on 2021-03-12 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0011_auto_20210306_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitorscript',
            name='frequency_delta',
            field=models.DurationField(default=datetime.timedelta(seconds=1800), help_text='How long to wait for the next execution, defaults to 30 minutes'),
        ),
        migrations.AlterField(
            model_name='monitorscript',
            name='status_code',
            field=models.IntegerField(default=200),
        ),
    ]
