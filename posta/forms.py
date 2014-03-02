from django import forms
from posta.models import Mail, Template

class MailForm(forms.ModelForm):
    name = forms.CharField(max_length=140, help_text="Please enter a name for your email.")
    subject_line = forms.CharField(max_length=140, help_text="Please enter the subject line for your email.")
    target = forms.CharField(max_length=140, help_text="Who is this email going to?")
    date_scheduled = forms.DateField(help_text="When do you need this email sent?")
    template = forms.IntegerField(help_text="Select a Template")

    class Meta:
        model = Mail
        fields = ('name','subject_line','target','date_scheduled','template')
