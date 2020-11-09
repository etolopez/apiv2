# Generated by Django 3.1.2 on 2020-11-05 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0011_auto_20201006_0058'),
        ('notify', '0003_auto_20201105_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slackchannel',
            name='cohort',
            field=models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='admissions.cohort'),
        ),
    ]
