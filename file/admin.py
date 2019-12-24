from django.contrib import admin
from .models import file

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(file)