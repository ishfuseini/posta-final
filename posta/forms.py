from django import forms
from posta.models import Mail, Template
from django.contrib.auth.models import User

class MailCreateForm(forms.ModelForm):
    name = forms.CharField(max_length=140, help_text="Please enter a name for your email.")
    subject_line = forms.CharField(max_length=140, help_text="Please enter the subject line for your email.")
    target = forms.CharField(max_length=140, help_text="Who is this email going to?")
    date_scheduled = forms.DateField(help_text="When do you need this email sent?",
                                     widget=forms.TextInput(attrs={'id':'datepicker'}))    
    template = forms.ModelChoiceField(queryset=Template.objects.all(), help_text="Select a Template")
    mail_body = forms.CharField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Mail
        fields = ('name','subject_line','target','date_scheduled','template', 'mail_body')

class MailComposeForm(forms.ModelForm):
    mail_body = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Mail
        fields = ('mail_body')
        
class MailEditForm(forms.ModelForm):
<<<<<<< HEAD
    subject_line = forms.CharField(max_length=140, help_text="Please enter the subject line for your email.")
    target = forms.CharField(max_length=140, help_text="Who is this email going to?")
    date_scheduled = forms.DateField(help_text="When do you need this email sent?",
                                     widget=forms.TextInput(attrs={'id':'datepicker'}))  
    
    class Meta:
        model = Mail
        fields = ('subject_line','target','date_scheduled')
=======
    pass

    class Meta:
        model = Mail
    	fields = ('subject_line','target','date_scheduled','template')
>>>>>>> ec54e5ec2cf2a1c0d7218e4e75de890e8bc9c366

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')        

