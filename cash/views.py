from rest_framework import generics

from .models import Currency, Query, Answer
from .serializers import CurrencySerializer, QuerySerializer, AnswerSerializer


class AnswerView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()


class QueryView(generics.ListCreateAPIView):
    serializer_class = QuerySerializer
    queryset = Query.objects.all()


class CurrencyListView(generics.ListCreateAPIView):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()





