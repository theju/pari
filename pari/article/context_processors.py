from .models import Type
from django.contrib.sites.requests import RequestSite


def types(request):
    return {'types': Type.objects.all()}


def sites(request):
    return {'site': RequestSite(request)}
