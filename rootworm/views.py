from rest_framework.decorators import api_view
from .models import Message
from .fields import MessageSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def messages(request):
    if request.method == 'GET':
        all_messages = Message.objects.all()
        serializer = MessageSerializer(all_messages, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
