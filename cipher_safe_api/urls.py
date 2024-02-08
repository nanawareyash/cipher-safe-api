from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="CipherSafe API",
        default_version="v1.0",
    ),
    public=False,
    authentication_classes=[BasicAuthentication],
    permission_classes=[permissions.IsAdminUser],
)

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # Swagger UI
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # Accounts App URLs
    path("accounts/", include("accounts.urls")),
]
