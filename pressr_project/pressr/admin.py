from django.contrib import admin
from .models import User, Reading, Comment, Provider

# Register your models here.

admin.site.register(User)
admin.site.register(Reading)
admin.site.register(Comment)
admin.site.register(Provider)
