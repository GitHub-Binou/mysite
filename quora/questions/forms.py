from django import forms
from quora.questions.models import Question

QUESTION_PLACEHOLDER = '说出你的问题'
SUMMARY_PLACEHOLDER = '问题的说明，请不要发表与留学，移民或培训无关的内容。'
TAG_PLACEHODER = '留学 移民'


class QuestionForm(forms.ModelForm):
    status = forms.CharField(widget=forms.HiddenInput())
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control input-lg',
            'placeholder': QUESTION_PLACEHOLDER,
        }),
        max_length=255,
        label='标题',)
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': SUMMARY_PLACEHOLDER}),
        max_length=4000,
        required=False,
        label='内容')
    tags = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': TAG_PLACEHODER}),
        max_length=255,
        required=False,
        label='标签',
        help_text='使用空格来分隔标签')

    class Meta:
        model = Question
        fields = ['title', 'content', 'tags', 'status']
