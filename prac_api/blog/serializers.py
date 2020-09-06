from rest_framework import serializers
from .models import Album,Artist

class ArtistListSerializer(serializers.ModelSerializer):
    albums = serializers.StringRelatedField(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'name','albums']

class AlbumGETSerializer(serializers.ModelSerializer):

    # artist = ArtistListSerializer()

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist']

# class AlbumPOSTSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Album
#         fields = ['id', 'title', 'artist']