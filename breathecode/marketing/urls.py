from django.urls import path
from .views import (create_lead, sync_tags_with_active_campaign, sync_automations_with_active_campaign,
                    receive_facebook_lead, get_leads, get_leads_report, AcademyLeadView, AcademyWonLeadView,
                    AcademyTagView, AcademyAutomationView, activecampaign_webhook, googleads_enrollments,
                    googleads_csv, get_downloadable, ShortLinkView, create_lead_from_app, UTMView,
                    AcademyProcessView, AcademyAppView, AcademyAliasView, ActiveCampaignView, UploadView)
from rest_framework.authtoken import views

app_name = 'marketing'
urlpatterns = [
    path('lead', create_lead, name='lead'),
    path('app', AcademyAppView.as_view(), name='app'),
    path('app/<slug:app_slug>/lead', create_lead_from_app, name='app_slug_lead'),
    path('app/lead', create_lead_from_app, name='app_lead'),
    path('lead/all', get_leads, name='lead_all'),  # TODO: HERE
    path('academy/lead', AcademyLeadView.as_view(), name='academy_lead'),
    path('academy/upload', UploadView.as_view(), name='upload'),
    path('academy/lead/<int:lead_id>', AcademyLeadView.as_view(), name='academy_lead_id'),
    path('academy/lead/process', AcademyProcessView.as_view(), name='academy_process_lead'),
    path('academy/lead/won', AcademyWonLeadView.as_view(), name='academy_won_lead'),
    path('academy/app', AcademyAppView.as_view(), name='app'),
    path('academy/alias', AcademyAliasView.as_view(), name='alias'),
    path('academy/<int:academy_id>/tag/sync', sync_tags_with_active_campaign, name='academy_id_tag_sync'),
    path('academy/<int:academt_id>/automation/sync',
         sync_automations_with_active_campaign,
         name='academy_id_automation_sync'),
    path('academy/tag', AcademyTagView.as_view(), name='academy_tag'),
    path('academy/tag/<slug:tag_slug>', AcademyTagView.as_view(), name='academy_tag_slug'),
    path('academy/automation', AcademyAutomationView.as_view(), name='academy_automation'),
    path('academy/short', ShortLinkView.as_view(), name='short'),
    path('academy/short/<slug:short_slug>', ShortLinkView.as_view(), name='short-slug'),
    path('academy/utm', UTMView.as_view(), name='academy_utm'),
    path('facebook/lead', receive_facebook_lead, name='facebook_all'),
    path('report/lead', get_leads_report, name='report_lead'),
    path('downloadable', get_downloadable, name='downloadable'),
    path('downloadable/<str:slug>', get_downloadable, name='single_downloadable'),

    # path('report/summary', get_summary, name="report_summary"),
    path('activecampaign', ActiveCampaignView.as_view(), name='activecampaign'),
    path('activecampaign/<int:ac_id>', ActiveCampaignView.as_view(), name='activecampaign_id'),
    path('activecampaign/webhook/<int:ac_academy_id>', activecampaign_webhook, name='activecampaign_webhook'),
    path('activecampaign/webhook/<str:academy_slug>', activecampaign_webhook, name='activecampaign_webhook'),
    path('googleads/enrollments/<str:academy_slugs>', googleads_enrollments, name='activecampaign_webhook'),
    path('googleads/data', googleads_csv, name='googleads_csv')
]
