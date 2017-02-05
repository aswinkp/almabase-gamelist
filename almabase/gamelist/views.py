from django.shortcuts import render
from rest_framework import viewsets
from models import *
from serializers import *
from django.conf import settings

# Create your views here.
class DisableCSRFOnDebug(object):
    def process_request(self, request):
        if settings.DEBUG:
            setattr(request, '_dont_enforce_csrf_checks', True)

class Table8ViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    serializer_class = Table8Serializer
    queryset = Table8.objects.all()