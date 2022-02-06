from rest_framework import serializers

from countries.models import Currency, Country


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ["url", "code", "name"]


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    currencies = CurrencySerializer(many=True)

    class Meta:
        model = Country
        fields = ["url", "name", "alpha_2_code", "alpha_3_code", "currencies"]
