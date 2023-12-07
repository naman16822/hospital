from django.urls import path, include

from rest_framework.routers import DefaultRouter

from case.views import CaseViewSet

router = DefaultRouter()

router.register('', CaseViewSet, basename='case')

urlpatterns = [
    path('', include(router.urls)),
]
