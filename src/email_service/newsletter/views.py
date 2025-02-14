from django.shortcuts import render
from .forms import EmailCampaignForm
from .models import EmailCampaign, Subscriber, EmailOpenRecord
from .tasks import send_campaign
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone

def create_newsletter(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        html_content = request.POST.get('html_content')
        send_date = request.POST.get('send_date')
        subscribers = request.POST.get('subscribers')
        newsletter = EmailCampaign.objects.create(subject=subject, html_content=html_content, send_date=send_date, subscribers=subscribers)
        if not send_date:
            send_campaign(newsletter.id, subscribers.id)
        return render(request, 'create_newsletter.html')
    else:
        form = EmailCampaignForm()
    return render(request, 'create_newsletter.html', {'form': form})

TRANSPARENT_PIXEL = (
    b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'
    b'\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0cIDATx\x9cc````'
    b'\x00\x00\x00\x05\x00\x01\xa3%\xadU\x00\x00\x00\x00IEND\xaeB`\x82'
)

def track_open(request, campaign_id, subscriber_id):
    campaign = get_object_or_404(EmailCampaign, id=campaign_id)
    subscriber = get_object_or_404(Subscriber, id=subscriber_id)
    open_record, created = EmailOpenRecord.objects.get_or_create(
        campaign=campaign,
        subscriber=subscriber,
        defaults={'opened_at': timezone.now()}
    )
    if not created:
        open_record.opened_at = timezone.now()
        open_record.save()
    response = HttpResponse(content_type="image/png")
    response['Content-Length'] = len(TRANSPARENT_PIXEL)
    response.write(TRANSPARENT_PIXEL)
    return response
