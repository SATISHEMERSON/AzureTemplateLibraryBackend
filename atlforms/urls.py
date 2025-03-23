from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/v1/azureresources', views.getazureresources, name='getformdata'),
    path('api/v1/azureresources/<int:id>', views.getazureresourceformdata, name='getformdata'),
]
