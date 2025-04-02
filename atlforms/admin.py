from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . import models

# Register your models here.

class AzureResourcesAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'title']

class AzureResourceFormAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'azureresource__name']

class AzureResourceFormFieldsAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'type']

class AzureResourceFormFieldsRelAdmin(ImportExportModelAdmin):
    search_fields = ['azureresourceform__name', 'azureresourceformfields__name']

class AzureResourceFormFieldsOptionsAdmin(ImportExportModelAdmin):
    search_fields = ['name']

class AzureResourceFormFieldsOptionsRelAdmin(ImportExportModelAdmin):
    search_fields = ['azureresourceformfields__name', 'azureresourceformfieldsoptions__name']

class AzureResourceCreationFormAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'azureresource__name']

class AzureResourceCreationFormFieldsAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'type']

class AzureResourceCreationFormFieldsOptionsAdmin(ImportExportModelAdmin):
    search_fields = ['name']

admin.site.register(models.AzureResources, AzureResourcesAdmin)
admin.site.register(models.AzureResourceForm, AzureResourceFormAdmin)
admin.site.register(models.AzureResourceFormFields, AzureResourceFormFieldsAdmin)
admin.site.register(models.AzureResourceFormFieldsRel, AzureResourceFormFieldsRelAdmin)
admin.site.register(models.AzureResourceFormFieldsOptions, AzureResourceFormFieldsOptionsAdmin)
admin.site.register(models.AzureResourceFormFieldsOptionsRel, AzureResourceFormFieldsOptionsRelAdmin)
admin.site.register(models.AzureResourceCreationForm, AzureResourceCreationFormAdmin)
admin.site.register(models.AzureResourceCreationFormFields, AzureResourceCreationFormFieldsAdmin)
admin.site.register(models.AzureResourceCreationFormFieldsOptions, AzureResourceCreationFormFieldsOptionsAdmin)
