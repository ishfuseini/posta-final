from django.db import models

# Create your models here.
  


class Mail(models.Model):
    DRAFT = 0
    READY = 1
    SENT = 2
    STATUS_CHOICES= ((DRAFT, 'Draft'),(READY, 'Ready'), (SENT, 'Sent'))
    name = models.CharField(max_length=140)
    date_created = models.DateTimeField(auto_now=True)
    date_scheduled = models.DateField()
    target = models.CharField(max_length=140)
    template = models.ForeignKey('Template')
    subject_line = models.CharField(max_length=140)
    mail_body = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES,default=DRAFT)

class Template(models.Model):
    template_body = models.TextField()


