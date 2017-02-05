from rest_framework import serializers
from models import Table8
from django.contrib.auth.models import User

class Table8Serializer(serializers.ModelSerializer):
    class Meta:
        model = Table8
        fields = ('title','platform','score','genre','editors_choice')




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('password', 'first_name', 'last_name', 'username', 'email')
#         write_only_fields = ('password',)
#         read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined',)
#
#     def restore_object(self, attrs, instance=None):
#         # call set_password on user object. Without this
#         # the password will be stored in plain text.
#         user = super(UserSerializer, self).restore_object(attrs, instance)
#         user.set_password(attrs['password'])
#         return user

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('password', 'first_name', 'last_name', 'username', 'email')