"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Admin URL
    path("admin/", admin.site.urls),
    # Web Pages URLs
    path("", include("books.urls")),
    # Web API URLs
    path("api/book/", include("book.urls")),
    # Dynamic schema generation
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Documentation URLs
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]

# Endpoints
# http://127.0.0.1:5000/admin/
# http://127.0.0.1:5000/api/book/
# http://127.0.0.1:5000/schema/
# http://127.0.0.1:5000/redoc/
# http://127.0.0.1:5000/docs/

# python manage.py runserver 5000
