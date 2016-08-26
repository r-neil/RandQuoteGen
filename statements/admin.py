from django.contrib import admin

# Register your models here.
from . import models

class StatementAdmin(admin.ModelAdmin):
	list_display = ['quote', 'author', 'already_used']
	list_editable = ['already_used']

admin.site.register(models.Statement, StatementAdmin)