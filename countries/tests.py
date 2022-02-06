from django.test import TestCase

from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APIRequestFactory

from countries import utils
from countries.models import Country, Currency
from countries.serializers import CurrencySerializer, CountrySerializer


class TestCountriesApiViews(TestCase):
    client_class = APIClient

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        utils.bootstrap_data()

    def test_api_currency_filters(self):
        # Baseline
        url = reverse("country-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 5)

        # Currency filter
        url = f"{reverse('country-list')}?currency=ZAR"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["alpha_2_code"], "ZA")

        url = f"{reverse('country-list')}?currency=TRL"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)

        # We can assume order as we are not altering the default ORM ordering
        # behaviour during create or read.
        self.assertEqual(response.data[0]["alpha_2_code"], "CY")
        self.assertEqual(response.data[1]["alpha_2_code"], "TR")

    def test_api_country_filter(self):
        # Baseline
        url = reverse("country-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 5)

        # Currency filter
        url = f"{reverse('country-list')}?country=TUR"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["alpha_2_code"], "TR")
        self.assertEqual(response.data[0]["alpha_3_code"], "TUR")

        url = f"{reverse('country-list')}?country=ZA"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["alpha_2_code"], "ZA")
        self.assertEqual(response.data[0]["alpha_3_code"], "ZAF")

        # Default behaviour uses the last country in the list to filter on.
        url = f"{reverse('country-list')}?country=CY&country=TUR"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["alpha_2_code"], "TR")
        self.assertEqual(response.data[0]["alpha_3_code"], "TUR")

    def test_all_filters(self):
        # Baseline
        url = reverse("country-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 5)

        url = f"{reverse('country-list')}?currency=TRL&country=CY"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["alpha_2_code"], "CY")

    def test_delete(self):
        country = Country.objects.first()

        # Baseline
        url = f"{reverse('country-list')}?country={country.alpha_2_code}"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], country.name)

        # Delete country
        self.assertTrue(country.active)
        url = f"{reverse('country-detail', {country.pk})}"
        response = self.client.delete(url)
        country.refresh_from_db()
        self.assertFalse(country.active)

        # Check the country is no longer returned by the api.
        url = f"{reverse('country-list')}?country={country.alpha_2_code}"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 0)
        self.assertNotIn(country.name, response.data)
        url = reverse("country-list")
        response = self.client.get(url)
        self.assertEqual(len(response.data), 4)


class TestCountriesApiSerializers(TestCase):
    client_class = APIClient

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        utils.bootstrap_data()

    def test_serializer_fields(self):
        currency = Currency.objects.first()
        request = APIRequestFactory().get(reverse("currency-list"))
        data = {
            "url": f"{request.build_absolute_uri()}{currency.pk}/",
            "code": currency.code,
            "name": currency.name,
        }
        serializer = CurrencySerializer(currency, context={"request": request})
        self.assertDictEqual(serializer.data, data)

        country = Country.objects.first()
        request = APIRequestFactory().get(reverse("country-list"))
        data = {
            "url": f"{request.build_absolute_uri()}{country.pk}/",
            "alpha_2_code": country.alpha_2_code,
            "alpha_3_code": country.alpha_3_code,
            "name": country.name,
            "currencies": [
                CurrencySerializer(currency, context={"request": request}).data
                for currency in country.currencies.all()
            ],
        }
        serializer = CountrySerializer(country, context={"request": request})
        self.assertDictEqual(serializer.data, data)
