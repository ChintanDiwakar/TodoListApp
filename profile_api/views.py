from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profile_api import serializers
from profile_api import models
from rest_framework.permissions import IsAuthenticated


from profile_api import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    # print("use")
    # queryset = models.ProfileFeedItem.objects.filter(user_profile.id == 1)
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated)

    def perform_create(self, serializers):
        serializers.save(user_profile=self.request.user)

    def get_queryset(self):
        user = self.request.user.id
        # print(user)
        listTasks = models.ProfileFeedItem.objects.all().filter(user_profile=user)

        return listTasks.all()
