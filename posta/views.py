from django.shortcuts import render
from django.http import HttpResponse
from posta.forms import MailForm
from django.shortcuts import render_to_response
from django.template import RequestContext
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

def mail(request, name_url):
    context = RequestContext(request)

    name = name_url.replace('_', ' ')
    context_dict = {'name' : name }
    try:
        name = Mail.objects.get(name=name)
        context_dict['name'] = name
    except Mail.DoesNotExist:
        pass
    return render_to_response('posta/mail.html', context_dict, context)



