"""
URL configuration for lrr project.

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
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("test/", TemplateView.as_view(template_name="test.html")),

    path('', include('core.urls')),

]
if settings.DEBUG:
    urlpatterns += [
        re_path(r"^static/(?P<path>.*)$", views.serve),
    ]

urlpatterns += staticfiles_urlpatterns()
