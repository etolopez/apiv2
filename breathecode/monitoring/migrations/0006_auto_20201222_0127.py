# Generated by Django 3.1.4 on 2020-12-22 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0007_auto_20201111_2218'),
        ('monitoring', '0005_auto_20201021_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='notify_slack_channel',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='notify.slackchannel'),
        ),
        migrations.AddField(
            model_name='application',
            name='paused_until',
            field=models.DateTimeField(blank=True, default=None, help_text='if you want to stop checking for a period of time', null=True),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='paused_until',
            field=models.DateTimeField(blank=True, default=None, help_text='if you want to stop checking for a period of time', null=True),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='special_status_text',
            field=models.CharField(blank=True, default=None, help_text='Add a message for people to see when is down', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='endpoint',
            name='status_text',
            field=models.CharField(blank=True, default=None, editable=False, max_length=255, null=True),
        ),
    ]