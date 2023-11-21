from django.urls import path
from .views import ExpenseAPIView, RemainAPIView, IncomeAPIView

urlpatterns = [
    path('remain/', RemainAPIView.as_view()),
    path('expense/', ExpenseAPIView.as_view()),
    path('expense/<int:pk>/', ExpenseAPIView.as_view()),
    path('income/', IncomeAPIView.as_view()),
    path('income/<int:pk>/', IncomeAPIView.as_view()),
]
