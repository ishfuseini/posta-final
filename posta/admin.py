from django.contrib import admin
from posta.models import Mail, mail_template, Image



# Register your models here.
admin.site.register(Mail)
admin.site.register(mail_template)
admin.site.register(Image)