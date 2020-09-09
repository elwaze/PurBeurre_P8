from django.contrib import admin

from pur_beurre.purbeurre_off import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'nutriscore', 'category', 'link',)
    list_filter = ('category__name',)
