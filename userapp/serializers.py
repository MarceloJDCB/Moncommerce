from rest_framework import serializers
from .models import User


class userSerializer(serializers.Serializer):
    username = serializers.CharField(
                                allow_null=False,
                                allow_blank=False,
                                required=True
                                     )
    password = serializers.CharField(
                                    allow_null=False,
                                    write_only=True,
                                    allow_blank=False,
                                    required=True
                                     )
    bananas = serializers.CharField()
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance.set_password(None)
        instance.save()
        return instance


    class Meta:
        model = User
        exclude = ['password']