"""
Test /academy/lead
"""
import re, string
from random import choice, choices, randint
from mixer.main import Mixer
from unittest.mock import patch
from django.urls.base import reverse_lazy
from rest_framework import status
from breathecode.tests.mocks import (
    GOOGLE_CLOUD_PATH,
    apply_google_cloud_client_mock,
    apply_google_cloud_bucket_mock,
    apply_google_cloud_blob_mock,
)
from ..mixins import MarketingTestCase

def random_string():
    return ''.join(choices(string.ascii_letters, k=10))

def generate_form_entry_kwargs():
    """That random values is too long that i prefer have it in one function"""
    return {
        'fb_leadgen_id': randint(0, 9999),
        'fb_page_id': randint(0, 9999),
        'fb_form_id': randint(0, 9999),
        'fb_adgroup_id': randint(0, 9999),
        'fb_ad_id': randint(0, 9999),
        'first_name': choice(['Rene', 'Albert', 'Immanuel']),
        'last_name': choice(['Descartes', 'Camus', 'Kant']),
        'email': choice(['a@a.com', 'b@b.com', 'c@c.com']),
        'phone': choice(['123', '456', '789']),
        'course': random_string(),
        'client_comments': random_string(),
        'location': random_string(),
        'language': random_string(),
        'utm_url': random_string(),
        'utm_medium': random_string(),
        'utm_campaign': random_string(),
        'utm_source': random_string(),
        'referral_key': random_string(),
        'gclid': random_string(),
        'tags': random_string(),
        'automations': random_string(),
        'street_address': random_string(),
        'country': random_string(),
        'city': random_string(),
        'latitude': randint(0, 9999),
        'longitude': randint(0, 9999),
        'state': random_string(),
        'zip_code': randint(0, 9999),
        'browser_lang': random_string(),

        'storage_status': choice(['PENDING', 'PERSISTED']),
        'lead_type': choice(['STRONG', 'SOFT', 'DISCOVERY']),
        'deal_status': choice(['WON', 'LOST']),
        'sentiment': choice(['GOOD', 'BAD']),
    }

class CohortUserTestSuite(MarketingTestCase):
    """Test /academy/lead"""

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_academy_lead_without_auth(self):
        """Test /cohort/:id/user without auth"""
        url = reverse_lazy('marketing:academy_lead')
        response = self.client.delete(url)
        json = response.json()
        expected = {
            'detail': 'Authentication credentials were not provided.',
            'status_code': 401
        }

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(self.all_form_entry_dict(), [])

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_academy_lead_without_args_in_url_or_bulk(self):
        """Test /cohort/:id/user without auth"""
        self.headers(academy=1)
        model = self.generate_models(authenticate=True, profile_academy=True,
            capability='crud_lead', role='potato')
        url = reverse_lazy('marketing:academy_lead')
        response = self.client.delete(url)
        json = response.json()
        expected = {
            'detail': "Missing parameters in the querystring",
            'status_code': 400
        }

        self.assertEqual(json, expected)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(self.all_form_entry_dict(), [])

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_academy_lead_in_bulk_with_one(self):
        """Test /cohort/:id/user without auth"""
        self.headers(academy=1)
        many_fields = ['id', 'fb_leadgen_id', 'fb_page_id', 'fb_form_id',
            'fb_adgroup_id', 'fb_ad_id', 'first_name', 'last_name', 'email',
            'phone', 'course', 'client_comments', 'location', 'language',
            'utm_url', 'utm_medium', 'utm_campaign', 'utm_source',
            'referral_key', 'gclid', 'tags', 'automations', 'street_address',
            'country', 'city', 'latitude', 'longitude', 'state', 'zip_code',
            'browser_lang', 'storage_status', 'lead_type', 'deal_status',
            'sentiment']

        base = self.generate_models(authenticate=True, profile_academy=True,
            capability='crud_lead', role='potato', academy=True,
            active_campaign_academy=True)

        for field in many_fields:
            form_entry_kwargs = generate_form_entry_kwargs()
            model = self.generate_models(form_entry=True, contact=True,
                automation=True, form_entry_kwargs=form_entry_kwargs, models=base)

            url = (reverse_lazy('marketing:academy_lead') + f'?{field}=' +
                str(getattr(model['form_entry'], field)))
            response = self.client.delete(url)

            if response.status_code != 204:
                print(response.json())

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(self.all_form_entry_dict(), [])

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_academy_lead_in_bulk_with_two(self):
        """Test /cohort/:id/user without auth"""
        self.headers(academy=1)
        many_fields = ['id', 'fb_leadgen_id', 'fb_page_id', 'fb_form_id',
            'fb_adgroup_id', 'fb_ad_id', 'first_name', 'last_name', 'email',
            'phone', 'course', 'client_comments', 'location', 'language',
            'utm_url', 'utm_medium', 'utm_campaign', 'utm_source',
            'referral_key', 'gclid', 'tags', 'automations', 'street_address',
            'country', 'city', 'latitude', 'longitude', 'state', 'zip_code',
            'browser_lang', 'storage_status', 'lead_type', 'deal_status',
            'sentiment']

        base = self.generate_models(authenticate=True, profile_academy=True,
            capability='crud_lead', role='potato', academy=True,
            active_campaign_academy=True)

        for field in many_fields:
            form_entry_kwargs = generate_form_entry_kwargs()
            model1 = self.generate_models(form_entry=True, contact=True,
                automation=True, form_entry_kwargs=form_entry_kwargs, models=base)

            form_entry_kwargs = generate_form_entry_kwargs()
            model2 = self.generate_models(form_entry=True, contact=True,
                automation=True, form_entry_kwargs=form_entry_kwargs, models=base)

            url = (reverse_lazy('marketing:academy_lead') + f'?{field}=' +
                str(getattr(model1['form_entry'], field)) + ',' +
                str(getattr(model2['form_entry'], field)))
            response = self.client.delete(url)

            if response.status_code != 204:
                print(response.json())

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(self.all_form_entry_dict(), [])

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_academy_lead_in_bulk_with_one_relationships(self):
        """Test /cohort/:id/user without auth"""
        self.headers(academy=1)
        many_fields = ['contact', 'academy', 'ac_academy', 'automation_objects']

        base = self.generate_models(authenticate=True, profile_academy=True,
            capability='crud_lead', role='potato', academy=True,
            active_campaign_academy=True)

        for field in many_fields:
            model = self.generate_models(form_entry=True, contact=True,
                automation=True, models=base)
            model['ac_academy'] = model['active_campaign_academy']
            model['automation_objects'] = model['automation']

            url = reverse_lazy('marketing:academy_lead') + f'?{field}=' + str(model[field].id)
            response = self.client.delete(url)

            if response.status_code != 204:
                print(response.json())

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(self.all_form_entry_dict(), [])

    @patch(GOOGLE_CLOUD_PATH['client'], apply_google_cloud_client_mock())
    @patch(GOOGLE_CLOUD_PATH['bucket'], apply_google_cloud_bucket_mock())
    @patch(GOOGLE_CLOUD_PATH['blob'], apply_google_cloud_blob_mock())
    def test_academy_lead_in_bulk_with_two_relationships(self):
        """Test /cohort/:id/user without auth"""
        self.headers(academy=1)
        many_fields = ['contact', 'academy', 'ac_academy', 'automation_objects']

        base = self.generate_models(authenticate=True, profile_academy=True,
            capability='crud_lead', role='potato', academy=True,
            active_campaign_academy=True)

        for field in many_fields:
            model1 = self.generate_models(form_entry=True, contact=True,
                automation=True, models=base)
            model1['ac_academy'] = model1['active_campaign_academy']
            model1['automation_objects'] = model1['automation']

            model2 = self.generate_models(form_entry=True, contact=True,
                automation=True, models=base)
            model2['ac_academy'] = model2['active_campaign_academy']
            model2['automation_objects'] = model2['automation']

            url = (reverse_lazy('marketing:academy_lead') + f'?{field}=' +
                str(model1[field].id) + ',' + str(model2[field].id))
            response = self.client.delete(url)

            if response.status_code != 204:
                print(response.json())

            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
            self.assertEqual(self.all_form_entry_dict(), [])
