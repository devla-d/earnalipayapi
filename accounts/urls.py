from django.urls import path
from .views import RegisterUserAPIView,ObtainAuthTokenView


urlpatterns = [
  
  
  path('register/',RegisterUserAPIView.as_view()),
  path('login/',ObtainAuthTokenView.as_view())

  
]
