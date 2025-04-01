from django.db import models

# Create your models here.

class AzureResources(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    imageURL = models.URLField(max_length=200)

    def __str__(self):
        return self.name

class AzureResourceForm(models.Model):
    name = models.CharField(max_length=100)
    azureresource = models.OneToOneField(AzureResources, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class AzureResourceFormFields(models.Model):
    INPUT_TYPE = (
        ('select', 'Select'),
        ('text', 'Text'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=INPUT_TYPE, default='txt')

    def __str__(self):
        return self.name

class AzureResourceFormFieldsRel(models.Model):
    azureresourceform = models.ForeignKey(AzureResourceForm, on_delete=models.CASCADE)
    azureresourceformfields = models.ForeignKey(AzureResourceFormFields, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.azureresourceformfields.name + ' - ' + self.azureresourceform.name

class AzureResourceFormFieldsOptions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class AzureResourceFormFieldsOptionsRel(models.Model):
    azureresourceformfields = models.ForeignKey(AzureResourceFormFields, on_delete=models.CASCADE)
    azureresourceformfieldsoptions = models.ForeignKey(AzureResourceFormFieldsOptions, on_delete=models.CASCADE)
    order = models.IntegerField()

    def __str__(self):
        return self.azureresourceformfields.name + ' - ' + self.azureresourceformfieldsoptions.name
    
class AzureResourceCreationFormFieldsOptions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AzureResourceCreationFormFields(models.Model):
    INPUT_TYPE = (
        ('select', 'Select'),
        ('text', 'Text'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=INPUT_TYPE, default='txt')
    options = models.ManyToManyField(AzureResourceCreationFormFieldsOptions, blank=True)

    def __str__(self):
        return self.name
    
class AzureResourceCreationForm(models.Model):
    name = models.CharField(max_length=100)
    azureresource = models.OneToOneField(AzureResources, on_delete=models.CASCADE)
    formfields = models.ManyToManyField(AzureResourceCreationFormFields, blank=True)

    def __str__(self):
        return self.name
    
