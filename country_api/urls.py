from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from countries import views


router = routers.DefaultRouter()
router.register(r"currencies", views.CurrencyViewSet)
router.register(r"countries", views.CountryViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
