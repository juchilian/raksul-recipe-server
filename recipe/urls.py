from django.urls import path
from .views import RecipeView, RecipeDetail

urlpatterns = [
    path('recipes/', RecipeView.as_view()),
    path('recipes/<int:pk>/', RecipeDetail.as_view()),
]