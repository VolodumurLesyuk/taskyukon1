from django.urls import path

from .views import CurrencyListView, QueryView, AnswerView


urlpatterns = [
    path('', CurrencyListView.as_view()),
    path('query/', QueryView.as_view()),
    path('answer/', AnswerView.as_view())
]