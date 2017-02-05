from django.shortcuts import render
from rest_framework import viewsets
from models import *
from serializers import *
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
class DisableCSRFOnDebug(object):
    def process_request(self, request):
        if settings.DEBUG:
            setattr(request, '_dont_enforce_csrf_checks', True)

class Table8ViewSet(viewsets.ModelViewSet, DisableCSRFOnDebug):
    authentication_classes = (SessionAuthentication, BasicAuthentication, JSONWebTokenAuthentication)
    permission_classes = (IsAuthenticated,)

    serializer_class = Table8Serializer
    queryset = Table8.objects.all()


from .permissions import IsStaffOrTargetUser


class UserView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    model = User
    queryset = User.objects.all()

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny()),
