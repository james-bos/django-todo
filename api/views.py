import json
import requests
from django.contrib.auth.models import User, Group
from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import filters
from api.models import PaginatedRawQuerySet
from users.models import Blog
from .serializers import UserSerializer, GroupSerializer, BlogSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blogs to be viewed or edited.
    """
    search_fields = ['title', 'content']
    filter_backends = (filters.SearchFilter,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
