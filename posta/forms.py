from django import forms
from posta.models import Mail, mail_template
from django.contrib.auth.models import User

class MailForm(forms.ModelForm):
    name = forms.CharField(max_length=140, help_text="Please enter a name for your email.")
    subject_line = forms.CharField(max_length=140, help_text="Please enter the subject line for your email.")
    target = forms.CharField(max_length=140, help_text="Who is this email going to?")
    date_scheduled = forms.DateField(help_text="When do you need this email sent?",
                                     widget=forms.TextInput(attrs={'id':'datepicker'}))    
    template = forms.ModelChoiceField(queryset=mail_template.objects.all(), help_text="Select a Template", widget=forms.RadioSelect)
    headline = forms.CharField(max_length=140, help_text="Please enter a headline for your email.")
    mail_body = forms.CharField(widget=forms.Textarea)
    image = forms.CharField(widget=forms.TextInput)
    button_url = forms.URLField()
    
    class Meta:
        model = Mail
        fields = ('name','subject_line','target','date_scheduled','template', 'headline', 'image', 'mail_body')
        #You can use widgets in the metafield. Look it up!


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')        

