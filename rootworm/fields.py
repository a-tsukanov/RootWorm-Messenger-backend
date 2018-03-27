from rest_framework import serializers
from . import models


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username')

    class Meta:
        model = models.Message
        fields = ('text', 'datetime', 'sender_name')