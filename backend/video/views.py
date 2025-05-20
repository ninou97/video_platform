from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Video
from .serializers import VideoSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать/удалять видео, только если он его владелец.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS запросы всем
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешить PUT, DELETE только владельцу
        return obj.owner == request.user

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Только аутентифицированные могут создавать
    parser_classes = [MultiPartParser, FormParser] # Для обработки загрузки файлов

    def perform_create(self, serializer):
        # При создании видео автоматически установить владельца на текущего пользователя
        serializer.save(owner=self.request.user)

class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [IsOwnerOrReadOnly] # Только владелец может редактировать/удалять
    parser_classes = [MultiPartParser, FormParser] # Для обработки загрузки файлов (если нужно обновлять файл)
