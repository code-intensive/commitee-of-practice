from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views import defaults as default_views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from src.config.routes.utils import prefix_api_endpoint
from src.users.api.urls import user_router

auth_view_routes = [
    path("auth/views/", include("rest_framework.urls")),
]

core_api_routes = [
    path(prefix_api_endpoint("auth"), include("auth.api.urls")),
    path(prefix_api_endpoint("users"), include(user_router.urls)),
]

open_api_routes = [
    path(
        prefix_api_endpoint("schema/download"),
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        prefix_api_endpoint("schema/swagger-ui"),
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        prefix_api_endpoint("schema/redoc"),
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns = sum([auth_view_routes, core_api_routes, open_api_routes], [])

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ] + static(
        settings.MEDIA_URL, document_root=settings.STATIC_URL
    )  # type: ignore