from rest_framework import serializers
from .models import TransmittedURL

class ShortURLSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = TransmittedURL
        fields = "__all__"

    def get_short_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(f'/{obj.short_id}')
