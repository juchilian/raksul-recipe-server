from django.http.response import Http404
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
    
    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Recipe successfully created!", "recipes": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost"}, status=status.HTTP_400_BAD_REQUEST)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404
            # raise Response({ "message":"No Recipe found" }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response({"message": "Recipe details by id", "recipe": [serializer.data]}, status=status.HTTP_200_OK)

    def patch(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Recipe successfully updated!", "recipe": serializer.errors}, status=status.HTTP_200_OK)
        return Response({"message": "Recipe creation failed!", "required": "title, making_time, serves, ingredients, cost"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response({"message": "Recipe successfully removed!"}, status=status.HTTP_204_NO_CONTENT)