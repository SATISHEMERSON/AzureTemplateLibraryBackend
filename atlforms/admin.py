from django.contrib import admin
from . import models

# Register your models here.

class AzureResourcesAdmin(admin.ModelAdmin):
    search_fields = ['name', 'title']

class AzureResourceFormAdmin(admin.ModelAdmin):
    search_fields = ['name', 'azureresource__name']

class AzureResourceFormFieldsAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type']

class AzureResourceFormFieldsRelAdmin(admin.ModelAdmin):
    search_fields = ['azureresourceform__name', 'azureresourceformfields__name']

class AzureResourceFormFieldsOptionsAdmin(admin.ModelAdmin):
    search_fields = ['name']

class AzureResourceFormFieldsOptionsRelAdmin(admin.ModelAdmin):
    search_fields = ['azureresourceformfields__name', 'azureresourceformfieldsoptions__name']

admin.site.register(models.AzureResources, AzureResourcesAdmin)
admin.site.register(models.AzureResourceForm, AzureResourceFormAdmin)
admin.site.register(models.AzureResourceFormFields, AzureResourceFormFieldsAdmin)
admin.site.register(models.AzureResourceFormFieldsRel, AzureResourceFormFieldsRelAdmin)
admin.site.register(models.AzureResourceFormFieldsOptions, AzureResourceFormFieldsOptionsAdmin)
admin.site.register(models.AzureResourceFormFieldsOptionsRel, AzureResourceFormFieldsOptionsRelAdmin)