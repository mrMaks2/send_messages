from celery import shared_task
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import request
from .models import EmailCampaign, Subscriber
from celery.task import periodic_task
from datetime import timedelta
from django.utils import timezone

@shared_task
def send_campaign(campaign_id, subscriber_id):
    campaign = EmailCampaign.objects.get(id=campaign_id)
    tracking_url = request.build_absolute_uri(
        reverse('track_open', args=[campaign_id, subscriber_id])
    )
    html_content = campaign.html_content.replace('{{ tracking_url }}', tracking_url)
    if not campaign.is_sent:
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            message = campaign.html_content.format(
                first_name=subscriber.first_name,
                last_name=subscriber.last_name,
                birthday=subscriber.birthday
            )
            send_mail(
                campaign.subject,
                message,
                'you@example.com',
                [subscriber.email],
                fail_silently=False,
                html_message=html_content
            )
        campaign.is_sent = True
        campaign.save()

@periodic_task(run_every=timedelta(minutes=60))
def schedule_emails():
    campaigns = EmailCampaign.objects.filter(is_sent=False)
    subscriber = campaigns.subscribers
    for campaign in campaigns:
        if campaign.send_date <= timezone.now():
            send_campaign(campaign.id, subscriber.id)