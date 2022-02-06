from countries.models import Currency, Country


def bootstrap_data():
    """Quick and dirty idempotent data bootstrapper."""
    currencies = [
        {
            "code": "AED",
            "name": "United Arab Emirates dirham",
        },
        {
            "code": "ZAR",
            "name": "South African rand",
        },
        {
            "code": "ZWL",
            "name": "Zimbabwean dollar",
        },
        {
            "code": "ZWR",
            "name": "Zimbabwean dollar",
        },
        {
            "code": "ZWN",
            "name": "Zimbabwean dollar",
        },
        {
            "code": "CYP",
            "name": "Cypriot pound",
        },
        {
            "code": "TRL",
            "name": "Turkish lira",
        },
        {
            "code": "TRL",
            "name": "Turkish lira",
        },
    ]
    countries = [
        {
            "name": "United Arab Emirates",
            "alpha_2_code": "AE",
            "alpha_3_code": "ARE",
            "currencies": [
                "AED",
            ],
        },
        {
            "name": "South Africa",
            "alpha_2_code": "ZA",
            "alpha_3_code": "ZAF",
            "currencies": ["ZAR"],
        },
        {
            "name": "Zimbabwe",
            "alpha_2_code": "ZW",
            "alpha_3_code": "ZWE",
            "currencies": ["ZWL", "ZWR", "ZWN"],
        },
        {
            "name": "Cyprus",
            "alpha_2_code": "CY",
            "alpha_3_code": "CYP",
            "currencies": ["CYP", "TRL"],
        },
        {
            "name": "Turkey",
            "alpha_2_code": "TR",
            "alpha_3_code": "TUR",
            "currencies": ["TRL"],
        },
    ]
    for currency in currencies:
        Currency.objects.update_or_create(**currency)
    for country in countries:
        currency_codes = country.pop("currencies", [])
        tup = Country.objects.update_or_create(**country)
        obj = tup[0]
        for currency_code in currency_codes:
            obj.currencies.add(Currency.objects.get(code=currency_code))
