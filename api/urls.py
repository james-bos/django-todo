from django.urls import include, path
from rest_framework import routers
from api.views import UserViewSet, GroupViewSet, BlogViewSet
from rest_framework.response import Response

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)
router.register('blogs', BlogViewSet)

# Setup automatic URL routing
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]