from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mail(models.Model):
    DRAFT = 0
    READY = 1
    SENT = 2
    STATUS_CHOICES= ((DRAFT, 'Draft'),(READY, 'Ready'), (SENT, 'Sent'))
    name = models.CharField(max_length=140, unique=True)
    date_created = models.DateTimeField(auto_now=True)
    date_scheduled = models.DateField()
    target = models.CharField(max_length=140)
    template = models.ForeignKey('mail_template')
    subject_line = models.CharField(max_length=140)
    headline = models.CharField(max_length=140)
    mail_body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT)
    image = models.URLField(null=True)
    created_by = models.ForeignKey(User)
    button_url = models.TextField(null=True)
    
    def __unicode__(self):
        return self.name


#TODO: Rename to MailTemplate
class mail_template(models.Model):
    name = models.TextField()
    template_body = models.TextField()
    
    def __unicode__(self):
        return self.name




