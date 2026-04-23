from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BookViewSet, AthenaeumViewSet

router_v1 = DefaultRouter()
router_v1.register('books', BookViewSet)
router_v1.register('athenaeum', AthenaeumViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
]
