"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    APIStructureView,
    secureResourceMediaView,
    secureProfileImageMediaView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


urlpatterns = []

if settings.DEBUG:
    urlpatterns = [
        path("api/", APIStructureView.as_view()),
        path("api/account/", include("account.urls")),
        path("admin/", admin.site.urls),
        path("api/courseAPI/", include("course.urls")),
        path("api/deadlineAPI/", include("deadline.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns = [
        path("api/", APIStructureView.as_view()),
        path("api/account/", include("account.urls")),
        path("admin/", admin.site.urls),
        path("api/courseAPI/", include("course.urls")),
        path("api/deadlineAPI/", include("deadline.urls")),
        path(
            "media/course_<int:course_pk>/<str:file_uuid>_<str:model_name>_<str:file_name>",
            secureResourceMediaView.as_view(),
        ),
        path("media/img/<str:image_name>", secureProfileImageMediaView.as_view())
    ]