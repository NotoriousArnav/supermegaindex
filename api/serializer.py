from rest_framework import serializers
from index.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'
        read_only_fields = ['user']


from django.contrib.auth import authenticate
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if not user:
            msg = 'Unable to authenticate with the provided credentials.'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
