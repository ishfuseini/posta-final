from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from posta.forms import MailForm
from django.shortcuts import render_to_response, get_object_or_404
from django.template import *
from django.template.loader import *
from django.contrib.auth.decorators import login_required
from posta.models import *
from django.contrib.formtools.preview import FormPreview
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def schedule(request):
    context = RequestContext(request)
    #Pass Current Emails to Template
    all_mail = Mail.objects.all()
    context_dict = {'emails' : all_mail } 
    for mail in all_mail:    
        mail.url = mail.id  
    return render_to_response('schedule.html', context_dict, context)

@login_required
def mail(request):
    context = RequestContext(request)
    all_mail = Mail.objects.all()
    context_dict = {'emails' : all_mail } 
    for mail in all_mail:    
        mail.url = mail.id
    return render_to_response('mail.html', context_dict, context)

  
@login_required
def mail_create(request):    
    context = RequestContext(request)
    if request.method == 'POST':
        form = MailForm(request.POST)         
        if form.is_valid():
          if '_preview' in request.POST:
              email = form.save(commit=False)
              template_body = form.cleaned_data['template'].template_body
              template = Template(template_body)             # <--
              return HttpResponse(template.render(Context({'mail':email})))
          elif '_save' in request.POST:
              form.save(commit=True)
              return HttpResponseRedirect(reverse('posta.mail'))
        else:
            print form.errors
    else:
        form = MailForm()       
    return render_to_response('mail_create.html', {'form' : form}, context)

  
@login_required
def mail_edit(request, mail_id):
    #TODO: Right now anybody can edit any mail
    #      Make is so you can only edit your own!
    context = RequestContext(request)
    mail = get_object_or_404(Mail, pk=mail_id)
    context_dict = {} 
    context_dict['mail'] = mail    
    
    if request.method == 'POST':       
        form = MailForm(request.POST, instance=mail)        
        if form.is_valid():
            form.save(commit=True)            
            return HttpResponseRedirect(reverse('posta.mail'))
        else:
            print form.errors
    else:
        form = MailForm(instance=mail)
        context_dict['form'] = form
        
    return render_to_response('mail_edit.html', context_dict, context)
  
@login_required
def mail_preview(request, mail_id):
    mail = get_object_or_404(Mail, pk=mail_id)
    subject_line =  mail.subject_line
    headline = mail.headline
    mail_body = mail.mail_body
    image = mail.image.image
    context_dict = {'mail' : mail} 
    context_dict['subject_line'] = subject_line
    context_dict['headline'] = headline
    context_dict['mail_body'] = mail_body
    context_dict['image'] = image 
    t = Template(mail.template.template_body)
    preview = t.render(Context(context_dict))
    return HttpResponse(preview)
  