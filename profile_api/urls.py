from django.urls import path
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
# from profile_api import views

router = DefaultRouter()
# router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet, basename='feeds')

urlpatterns = [
    # path('hello-view/', views.mainProfile.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
