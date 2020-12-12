from django.urls import path, include

from snippets import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('snippets', views.SnippetViewSet)
router.register('users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
