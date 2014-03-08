from django.contrib import admin
from posta.models import Mail, Template, Image



# Register your models here.
admin.site.register(Mail)
admin.site.register(Template)
admin.site.register(Image)