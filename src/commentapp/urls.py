from django.urls import path
from .views import *

urlpatterns = [
    path("",CreateAndGetAllComment.as_view()),
]