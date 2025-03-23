from rest_framework import serializers
from .models import (
    AzureResources,
    AzureResourceForm,
    AzureResourceFormFields,
    AzureResourceFormFieldsRel,
    AzureResourceFormFieldsOptions,
    AzureResourceFormFieldsOptionsRel
)

class AzureResourceFormFieldsOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzureResourceFormFieldsOptions
        fields = '__all__'

class AzureResourceFormFieldsOptionsRelSerializer(serializers.ModelSerializer):
    azureresourceformfieldsoptions = AzureResourceFormFieldsOptionsSerializer(read_only=True)

    class Meta:
        model = AzureResourceFormFieldsOptionsRel
        fields = ['id', 'azureresourceformfieldsoptions', 'order']

class AzureResourceFormFieldsSerializer(serializers.ModelSerializer):
    options = AzureResourceFormFieldsOptionsRelSerializer(many=True, read_only=True, source='azureresourceformfieldsoptionsrel_set')

    class Meta:
        model = AzureResourceFormFields
        fields = ['id', 'name', 'type', 'options']

class AzureResourceFormFieldsRelSerializer(serializers.ModelSerializer):
    azureresourceformfields = AzureResourceFormFieldsSerializer(read_only=True)

    class Meta:
        model = AzureResourceFormFieldsRel
        fields = ['id', 'azureresourceformfields', 'order']

class AzureResourceFormSerializer(serializers.ModelSerializer):
    fields = AzureResourceFormFieldsRelSerializer(many=True, read_only=True, source='azureresourceformfieldsrel_set')

    class Meta:
        model = AzureResourceForm
        fields = ['id', 'name', 'fields']

class AzureResourceSerializer(serializers.ModelSerializer):
    form = AzureResourceFormSerializer(read_only=True, source='azureresourceform')

    class Meta:
        model = AzureResources
        fields = ['id', 'name', 'title', 'imageURL', 'form']