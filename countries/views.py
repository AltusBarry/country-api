from rest_framework import viewsets
from rest_framework import permissions

from countries.models import Currency, Country
from countries.serializers import CurrencySerializer, CountrySerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    """Displays currency details."""

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CountryViewSet(viewsets.ModelViewSet):
    """Display country information as well as nested currency details.

    Can filter by currency code using queryparam; "currency". Supports multiple
    currencies being passed along.
    """

    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        """Override to facilitate filtering. This is the quickest method in
        DRF, by default.
        """
        queryset = super().get_queryset()

        currencies = self.request.query_params.getlist("currency")
        country_code = self.request.query_params.get("country")
        if currencies:
            queryset = queryset.filter(currencies__code__in=currencies)
        if country_code:
            code_filter = {}
            if len(country_code) == 2:
                code_filter = {"alpha_2_code": country_code}
            elif len(country_code) == 3:
                code_filter = {"alpha_3_code": country_code}
            queryset = queryset.filter(**code_filter)
        return queryset

    def perform_destroy(self, instance):
        """Prevents the object from being deleted, merely marks it as inactive."""
        instance.active = False
        instance.save()
