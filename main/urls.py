from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('header/',HeaderView.as_view()),
    path('category/',CategoryView.as_view()),
    path('subcategory/',SubCategoryView.as_view()),
    path('cards/',CardView.as_view()),
    path('card/<int:pk>/',CardDetailView.as_view()),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/',UserRegister.as_view()),
]