from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers
from datetime import datetime, timezone
import requests
import os
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getazureresources(request):
    data = models.AzureResources.objects.all()
    serializer = serializers.AzureResourceSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)

def getazureresourceformdata(request, id):
    try:
        resource = models.AzureResources.objects.get(id=id)
    except models.AzureResources.DoesNotExist:
        return JsonResponse({'error': 'Resource not found'}, status=404)

    serializer = serializers.AzureResourceSerializer(resource)
    return JsonResponse(serializer.data, safe=False)

def getazurecreationresourceformdata(request, id):
    print("hello")
    try:
        resource = models.AzureResources.objects.get(id=id)
    except models.AzureResources.DoesNotExist:
        return JsonResponse({'error': 'Resource not found'}, status=404)

    serializer = serializers.AzureResourceCreationSerializer(resource)
    data = serializer.data
    for i in range(len(data['form']['formfields'])):
        if data['form']['formfields'][i]['name'] == 'Subscription':
            data['form']['formfields'][i]['options'] = [
                {
                    'id': 1,
                    'name': 'sub-z-corp-test-n-003',
                }
            ]
        elif data['form']['formfields'][i]['name'] == 'Resource Group':
            data['form']['formfields'][i]['options'] = [
                {
                    'id': 1,
                    'name': 'rg-z-corp-isummit-atl-001',
                },
                {
                    'id': 2,
                    'name': 'rg-test-sa-isummit-n-001',
                }
            ]
    return JsonResponse(data, safe=False)

from .utils import openai
import json
@csrf_exempt
def cost_analysis(request):
    data = json.loads(request.body)
    new_data = {
        'useCase': data['useCase'] if 'useCase' in data else data['Storage purpose'],
        'accessfrequency': data['accessfrequency'] if 'accessfrequency' in data else data['Data Access Frequency'],
        'redundancy': data['redundancy'] if 'redundancy' in data else data['Redundancy Preference'],
        'performance': data['performance'] if 'performance' in data else data['Performance Requirement'],
        'budget': data['budget'] if 'budget' in data else data['Budget Constraint'],
        'usercomment': data['usercomment'] if 'usercomment' in data else data['User Comments'],
        'location': data['location'] if 'location' in data else data['Location'],
    }
    print(new_data)
    res = openai.cost_analysis(new_data)
    # # print(res)
    # res = {}
    res['Location'] = data['location'] if 'location' in data else data['Location']
    try:
        return JsonResponse(res, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Error in processing request'}, status=500)

@csrf_exempt
def resource_creation(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)
    data = json.loads(request.body)
    variables = {}
    variables['RequestNumber'] = {}
    variables['RequestNumber']['value'] = "RITM" + str(datetime.now(timezone.utc).timestamp()).split('.')[0]
    variables['RequestNumber']['isSecret'] = False
    variables['Subscription'] = {}
    variables['Subscription']['value'] = data['Subscription']
    variables['Subscription']['isSecret'] = False
    variables['resourcegroup'] = {}
    variables['resourcegroup']['value'] = data['Resource Group']
    variables['resourcegroup']['isSecret'] = False
    variables['storageaccountname'] = {}
    variables['storageaccountname']['value'] = data['Storage Account Name']
    variables['storageaccountname']['isSecret'] = False
    variables['sku'] = {}
    variables['sku']['value'] = data['sku']
    variables['sku']['isSecret'] = False
    variables['storageaccountkind'] = {}
    variables['storageaccountkind']['value'] = data['kind']
    variables['storageaccountkind']['isSecret'] = False
    variables['accesstier'] = {}
    variables['accesstier']['value'] = data['accessTier']
    variables['accesstier']['isSecret'] = False
    variables['location'] = {}
    variables['location']['value'] = str(data['Location']).replace(" ", "").lower()
    variables['location']['isSecret'] = False
    variables['Requester'] = {}
    variables['Requester']['value'] = 'rkaur@emerson.com'
    variables['Requester']['isSecret'] = False
    data = {
      'definitionId': 105,
      'description':
        "Service Now posted release triggered via curl with variables",
      'artifacts': [],
      'variables': variables,
    }
    api_endpoint = os.environ.get('AZURE_DEVOPS_API_ENDPOINT')
    token = "Bearer " + os.environ.get('AZURE_DEVOPS_API_KEY')
    response = requests.post(api_endpoint, headers={'Authorization': token}, json=data)
    print(response.status_code)
    # print(response.json())
    # useremail = data['useremail'] if 'useremail' in data else data['User Email']
    # return JsonResponse(data, safe=False)
    print("Called to create resource", variables)
    return JsonResponse({'message': 'Resource creation started'}, status=200)
