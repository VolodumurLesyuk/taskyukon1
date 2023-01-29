from rest_framework import serializers

from .models import Currency, Query, Answer


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('type', )


class QuerySerializer(serializers.ModelSerializer):
    give = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=Currency.objects.all())

    class Meta:
        model = Query
        fields = "__all__"

    def create(self, validated_data):
        query = Query.objects.create(**validated_data)
        return query


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"


