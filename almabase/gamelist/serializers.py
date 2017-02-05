from rest_framework import serializers
from models import Table8

class Table8Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table8
        fields = ('title','platform','score','genre','editors_choice')