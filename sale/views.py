# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from sale.serializers import ItemSerializer
from sale.models import Item
from rest_framework.renderers import JSONRenderer,AdminRenderer,TemplateHTMLRenderer, HTMLFormRenderer
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from django.views import View
from django.views.generic import TemplateView

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class ItemViewSet(viewsets.ModelViewSet):
    renderer_classes = (AdminRenderer, )
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer