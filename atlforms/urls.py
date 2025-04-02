from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/azureresources', views.getazureresources, name='getformdata'),
    path('api/v1/azureresources/<int:id>/form/requirements', views.getazureresourceformdata, name='getformdata'),
    path('api/v1/azureresources/<int:id>/form/creation', views.getazurecreationresourceformdata, name='getresourcecreationformdata'),
    path('api/v1/costanalysis', views.cost_analysis, name='costanalysis'),
    path('api/v1/resource', views.resource_creation, name='resourcrecreation'),
]
