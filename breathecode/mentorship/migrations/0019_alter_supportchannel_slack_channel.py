# Generated by Django 3.2.16 on 2023-01-23 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0010_auto_20220901_0323'),
        ('mentorship', '0018_chatbot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supportchannel',
            name='slack_channel',
            field=models.ForeignKey(blank=True,
                                    default=None,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='notify.slackchannel'),
        ),
    ]