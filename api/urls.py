from django.urls import path
from .views import index, WebhookView, Listener

urlpatterns = [
    path('',Listener.as_view()),
    path('index',index),
    path('view',WebhookView.as_view())
]
