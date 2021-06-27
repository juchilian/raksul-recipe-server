from .models import Recipe
from rest_framework import status
from .serializer import RecipeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class RecipeView(APIView):
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

class RecipeDetail(APIView):

    def get(self, request, pk, format=None):
        try:
            recipe = self.get_object(pk)
            serializer = RecipeSerializer(recipe)
            return Response({"message": "Recipe details by id", "recipe": [serializer.data]}, status=status.HTTP_200_OK)
        except:
            return Response({ "message":"No Recipe found" }, status=status.HTTP_404_NOT_FOUND)
 

    def patch(self, request, pk, format=None):
        try:
            recipe = self.get_object(pk)
            serializer = RecipeSerializer(recipe, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Recipe successfully updated!", "recipe": [serializer.data]}, status=status.HTTP_200_OK)

            return Response({"message": "Recipe update failed!", "required": "title, making_time, serves, ingredients, cost"}, status=status.HTTP_400_BAD_REQUEST)

        except:
            return Response({ "message":"No Recipe found" }, status=status.HTTP_404_NOT_FOUND)



    def delete(self, request, pk, format=None):
        try:
            recipe = self.get_object(pk)
            recipe.delete()
            return Response({"message": "Recipe successfully removed!"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({ "message":"No Recipe found" }, status=status.HTTP_404_NOT_FOUND)
