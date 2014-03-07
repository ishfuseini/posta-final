from django.shortcuts import render
from django.http import HttpResponse
from posta.forms import MailCreateForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from posta.models import *
from django.contrib.formtools.preview import FormPreview

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def schedule(request):
    return render(request, 'schedule.html')

@login_required
def mail(request):
    context = RequestContext(request)
    #Pass Current Emails to Template
    mail_name = Mail.objects.all()
    context_dict = {'emails' : mail_name } 
    for mail in mail_name:    
        mail.url = mail.id
    return render_to_response('mail.html', context_dict, context)

  
@login_required
def mail_create(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = MailCreateForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return mail(request)
        else:
            print form.errors
    else:
        form = MailCreateForm()
        
    return render_to_response('create.html', {'form' : form}, context)