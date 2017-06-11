from django import forms
from quora.events.models import Event

EVENT_PLACEHOLDER = '活动标题'
SUMMARY_PLACEHOLDER = '活动内容'


class EventForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-lg',
            'placeholder': EVENT_PLACEHOLDER,
        }),
        max_length=255,
        label='标题',)
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': SUMMARY_PLACEHOLDER}),
        max_length=4000,
        required=False,
        label='内容')

    class Meta:
        model = Event
        fields = ['title', 'content']
