import imp
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import Webhook
from .serializers import WebhookSerializer
# Create your views here.

def index(request):
    return HttpResponse("404")

class WebhookView(generics.ListCreateAPIView):
    queryset=Webhook.objects.all()
    serializer_class=WebhookSerializer

class Listener(APIView):
    def get(self,request,format=None):
        return HttpResponse("404")
    serializer_class=WebhookSerializer
    def post(self,request,format=None):
        # # qq = Request()
        # # qq.
        # print(request.META)
        requestData=request.data
        if requestData!=None:
            contentString = str(requestData)
            requestObject = Webhook(content=contentString)        
            requestObject.save()
            return Response({'Done'},status=status.HTTP_200_OK)
        return Response({'Bad Request:','Request parameter Not meant'},status=status.HTTP_400_BAD_REQUEST)
