from django.urls import path

from .views import CurrencyListView, QueryView, AnswerView


urlpatterns = [
    path('', CurrencyListView.as_view()),
    path('auf/', QueryView.as_view()),
    path('answer/', AnswerView.as_view())
]