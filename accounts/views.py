from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import GenericViewSet, ViewSet

from .models import Users
from .serializers import UserSerializer


class UserViewSet(ViewSet, GenericViewSet):
    queryset = Users.objects.all()
    parser_classes = [JSONParser]
    serializer_class = UserSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    # Get all users list
    def list(self, request):
        new_queryset = self.queryset.order_by("-created_at")
        page = self.paginate_queryset(new_queryset)

        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(page, many=True)

        if serializer:
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    # Create user
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account Created Successfully!"})
        else:
            return Response({"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    # Get particular user details
    @action(detail=True)
    def details(self, request, pk):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user)
        if serializer:
            return Response({"result": serializer.data})
        else:
            return Response({"errors": serializer.errors}, status=HTTP_400_BAD_REQUEST)
