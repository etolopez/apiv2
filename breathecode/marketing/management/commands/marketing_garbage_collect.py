from django.core.management.base import BaseCommand, CommandError
from ...tasks import persist_single_lead
from ...models import FormEntry
from django.contrib.auth.models import User
from django.db import connection


class Command(BaseCommand):
    help = 'Clean data from marketing module'

    def handle(self, *args, **options):

        self.delete_old_webhooks()

    def delete_old_webhooks(self):
        cursor = connection.cursor()
        #status = 'ERROR' or status = 'PENDING' AND
        cursor.execute(
            "DELETE FROM marketing_activecampaignwebhook WHERE created_at < NOW() - INTERVAL '30 days'")

        cursor.execute(
            "DELETE FROM marketing_activecampaignwebhook WHERE status <> 'ERROR' AND status <> 'PENDING'")
