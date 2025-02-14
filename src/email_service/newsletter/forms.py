# coding=utf-8
from django import forms
from .models import EmailCampaign, Subscriber


class EmailCampaignForm(forms.ModelForm):
    subject = forms.CharField(label='Тема',
                              widget=forms.TextInput(attrs={
                                  'class': 'form-control','placeholder': 'Введите тему рассылки'
                              }))
    html_content = forms.CharField(label='Объект рассылки',
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control', 'placeholder': 'Введите объект рассылки'
                                   }))
    send_date = forms.DateTimeField(label='Дата и время отправки',
                                    widget=forms.DateTimeInput(attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Введите дату и время (YYYY-MM-DD HH:MM)'}))
    subscribers = forms.ModelMultipleChoiceField(label='Выбор подписчиков',
                                            queryset=Subscriber.objects.all(),
                                            required=False,
                                            widget=forms.SelectMultiple(attrs={
                                                'class': 'form-control js-example-basic-multiple'}))
    class Meta:
        model = EmailCampaign
        fields = ['subject', 'html_content', 'send_date', 'subscribers']