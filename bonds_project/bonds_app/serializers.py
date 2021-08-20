from rest_framework import serializers

from .models import Bond


class BondSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bond
        fields = ('id','name', 'price', 'total')
