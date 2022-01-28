from django.db.models import Q
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from ..models import MMessage
from .serializers import MessageSerializer, NewMessageSerializer, UserSerializer, NewUserSerializer


class Pagination3(PageNumberPagination):
    page_size = 3


class SendView(APIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = self.request.user
        message = request.data.get('message')
        message['user_from'] = user.id
        serializer = NewMessageSerializer(data=message)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
            return Response({"success": "Message '{}' created successfully".format(saved.title)})


class RegisterView(APIView):

    def post(self, request):
        user = {
            'username': request.data.get('username', ''),
            'password': request.data.get('password', ''),
        }
        print(user)
        serializer = NewUserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
            return Response('ok')
            #return Response({"token": "{}".format(saved.username)})


class UsersView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = Pagination3


class MessagesView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination3

    def get_queryset(self):
        user = self.request.user
        queryset = super(MessagesView, self).get_queryset()
        queryset = queryset.filter(
            Q(user_to=user) | Q(user_from=user)
        )
        return queryset


class InboxView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination3

    def get_queryset(self):
        queryset = super(InboxView, self).get_queryset()
        queryset = queryset.filter(user_to=self.request.user)
        return queryset


class SentView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer
    pagination_class = Pagination3

    def get_queryset(self):
        queryset = super(SentView, self).get_queryset()
        queryset = queryset.filter(user_from=self.request.user)
        return queryset


class MessageDetailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    queryset = MMessage.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = super(MessageDetailView, self).get_queryset()
        queryset = queryset.filter(
            Q(user_to=user) | Q(user_from=user)
        )
        return queryset
