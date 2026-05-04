from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.travel_list, name='travel_list'),
    path('detail/<int:pk>/', views.travel_detail, name='travel_detail'),
    path('ai/', views.ai_recommend, name='ai_recommend'),
    path('ai/generate/', views.ai_generate, name='ai_generate'),
]