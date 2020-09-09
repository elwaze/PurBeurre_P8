from django.contrib import admin

from pur_beurre.purbeurre_results import models


@admin.register(models.Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'created', 'updated',)
