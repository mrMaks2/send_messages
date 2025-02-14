from __future__ import unicode_literals
from django.db import models

class Subscriber(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class EmailCampaign(models.Model):
    subject = models.CharField(max_length=255)
    html_content = models.TextField()
    send_date = models.DateTimeField(null=True, blank=True)
    subscribers = models.CharField(max_length=255)
    is_sent = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.subject, self.is_sent)

class EmailOpenRecord(models.Model):
    campaign = models.ForeignKey('EmailCampaign', on_delete=models.CASCADE)
    subscriber = models.ForeignKey('Subscriber', on_delete=models.CASCADE)
    opened_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Open record for {} by {}".format(self.campaign, self.subscriber)