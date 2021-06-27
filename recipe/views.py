from django.shortcuts import render
from .models import Recipe
from rest_framework import generics, serializers, status
from .serializer import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class RecipeView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer