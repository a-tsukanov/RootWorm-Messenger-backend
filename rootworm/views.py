from rest_framework.decorators import api_view
from .models import Message
from .fields import MessageSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def messages(request):
    if request.method == 'GET':
        all_messages = Message.objects.all()
        serializer = MessageSerializer(all_messages, many=True)
        return Response(serializer.data)
