"""
URL configuration for buzzer_game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from rest_framework import routers
from django.urls import path, include
from django.contrib import admin
from backend import views
from backend.views import index_view
from backend.views import PlayerViewSet, TeamViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r"users", PlayerViewSet)
router.register(r"team", TeamViewSet)
router.register(r"questions", QuestionViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("events/", views.sse_view, name="sse"),
    path("fe/", index_view, name="index"),  # Serve the HTML page
    path("api/", include("rest_framework.urls", namespace="rest_framework")),
]
