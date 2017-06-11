from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=30,
        required=True)
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
        max_length=75,
        required=False)

    class Meta:
        model = User
        fields = ['first_name', 'email']

    def full_clean(self):
        'Strip whitespace automatically in all form fields'
        data = self.data.copy()
        for k, vs in self.data.items():
            new_vs = []
            new_vs.append(vs.strip())
            data.setlist(k, new_vs)
        self.data = data
        super(ProfileForm, self).full_clean()


class ChangePasswordForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput())
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="旧密码",
        required=True)

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="新密码",
        required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="确认新密码",
        required=True)

    class Meta:
        model = User
        fields = ['id', 'old_password', 'new_password', 'confirm_password']

    def clean(self):
        super(ChangePasswordForm, self).clean()
        old_password = self.cleaned_data.get('old_password')
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')
        id = self.cleaned_data.get('id')
        user = User.objects.get(pk=id)
        if not user.check_password(old_password):
            self._errors['old_password'] = self.error_class(['输入的旧密码有误'])
        if new_password and new_password != confirm_password:
            self._errors['new_password'] = self.error_class(['两次输入的新密码不匹配'])
        return self.cleaned_data