from django.shortcuts import render
from django.http import HttpResponse
from posta.forms import MailForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from posta.models import Mail

def index(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = MailForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = MailForm()
    return render_to_response('index.html', {'form': form}, context)


def about(request):
    return render(request, 'about.html')

def schedule(request):
    return render(request, 'schedule.html')

@login_required
def mail(request):
    return render_to_response('mail.html', context_dict, context)
  
@login_required
def mail_create(request):
    #use your MailForm here
    return ""

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
