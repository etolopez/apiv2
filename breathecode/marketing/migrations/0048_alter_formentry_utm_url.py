# Generated by Django 3.2.9 on 2022-01-17 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0047_alter_leadgenerationapp_utm_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='utm_url',
            field=models.CharField(blank=True, default=None, max_length=2000, null=True),
        ),
    ]