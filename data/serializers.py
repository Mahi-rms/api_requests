from .models import Data
from rest_framework import serializers,fields

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'name','description','email','created_at')