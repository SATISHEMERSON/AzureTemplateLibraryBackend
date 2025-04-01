from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers

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
                    'name': 'Free Trial',
                },
                {
                    'id': 1,
                    'name': 'Pay-As-You-Go',
                },
                {
                    'id': 1,
                    'name': 'Enterprise Agreement',
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
        'security': data['security'] if 'security' in data else data['Security Preferences'],
        'usercomment': data['usercomment'] if 'usercomment' in data else data['User Comments'],
    }
    print(new_data)
    res = openai.cost_analysis(new_data)
    # # print(res)
    # res = {}
    try:
        return JsonResponse(res, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'error': 'Error in processing request'}, status=500)
