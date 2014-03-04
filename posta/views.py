from django.shortcuts import render
from django.http import HttpResponse
from posta.forms import MailForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from posta.models import Mail

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
    return render_to_response('mail.html', context_dict, context)
  
@login_required
def mail_create(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = MailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return mail_compose(request, mail_id)
        else:
            print form.errors
    else:
        form = MailForm()
        
    return render_to_response('create.html', {'form' : form}, context)

@login_required
def mail_edit(request, mail_id):
    #use your MailForm here
    return ""

@login_required
def mail_compose(request, mail_id):
    #we'll do this later usiny tinymce or ckeditor
    return ""
  
@login_required  
def mail_submit(request, mail_id):
    return ""
