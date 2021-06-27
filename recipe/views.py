from django.shortcuts import render
from .models import Recipe
from rest_framework import generics, serializers, status
from .serializer import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class RecipeView(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer

    def get(self, request, format=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        
        return Response({"recipes": serializer.data})

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer