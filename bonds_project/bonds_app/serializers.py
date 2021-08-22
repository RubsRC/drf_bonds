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

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Ensure this field has more than 3 characters")
        return value

    def validate_total(self, value):
        if value < 1:
            raise serializers.ValidationError(
                "Ensure this field is bigger than 0")
        if value > 10000:
            raise serializers.ValidationError(
                "Ensure this field is lower than 10,000")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Ensure this field is 0 or bigger")
        if value > 100000000.0000:
            raise serializers.ValidationError(
                "Ensure this field is lower than 100,000,000.0000")
        return value
