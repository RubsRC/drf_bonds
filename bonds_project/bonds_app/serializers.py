from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Bond


class UserSerializer(serializers.ModelSerializer):
    bonds = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'bonds']


class BondSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Bond
        fields = ('id', 'name', 'price', 'total', 'owner')
