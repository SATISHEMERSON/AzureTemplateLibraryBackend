from rest_framework import serializers
from .models import (
    AzureResources,
    AzureResourceForm,
    AzureResourceFormFields,
    AzureResourceFormFieldsRel,
    AzureResourceFormFieldsOptions,
    AzureResourceFormFieldsOptionsRel,
    AzureResourceCreationForm,
    AzureResourceCreationFormFields,
    AzureResourceCreationFormFieldsOptions,
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
        fields = ['id', 'name', 'type', 'helper_text', 'required', 'options']

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

class AzureResourceCreationFormFieldsOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AzureResourceCreationFormFieldsOptions
        fields = '__all__'

class AzureResourceCreationFormFieldsSerializer(serializers.ModelSerializer):
    options = AzureResourceCreationFormFieldsOptionsSerializer(many=True, read_only=True)

    class Meta:
        model = AzureResourceCreationFormFields
        fields = ['id', 'name', 'type', 'options']

class AzureResourceCreationFormSerializer(serializers.ModelSerializer):
    formfields = AzureResourceCreationFormFieldsSerializer(many=True, read_only=True)

    class Meta:
        model = AzureResourceCreationForm
        fields = ['id', 'name', 'formfields']

class AzureResourceCreationSerializer(serializers.ModelSerializer):
    form = AzureResourceCreationFormSerializer(read_only=True, source='azureresourcecreationform')

    class Meta:
        model = AzureResources
        fields = ['id', 'name', 'title', 'imageURL', 'form']
