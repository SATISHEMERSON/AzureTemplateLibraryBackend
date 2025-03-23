from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
from . import serializers

# Create your views here.

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