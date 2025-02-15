from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from movies.views import MovieViewSet, ActionViewSet,ComedyViewSet
from django.conf.urls.static import static
from django.conf import settings
router = routers.SimpleRouter()
router.register('movies', MovieViewSet)  # Uses default basename 'moviedata'
router.register('action', ActionViewSet, basename='action-movies')  # 
router.register('comedy', ComedyViewSet, basename='comedy-movies')  # Assigns a unique basename

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
