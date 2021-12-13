from rest_framework import serializers
from .models import Users, Developers, Apis


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= Users
        fields=('id', 'first_name', 'last_name', 'city')


class DevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Developers
        fields = '__all__'

        fields= (
            'developerName',
            'language',
            'company',
            'location'
        )

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apis
        fields='__all__'



class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model=[Users, Apis]
        fields='__all__'