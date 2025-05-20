from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # Показываем имя владельца, но не даем его менять

    class Meta:
        model = Video
        fields = '__all__' # Включает все поля модели
        read_only_fields = ['owner', 'upload_date']