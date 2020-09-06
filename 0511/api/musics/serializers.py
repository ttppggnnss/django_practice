from rest_framework import serializers
from .models import Artist, Music, Comment

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id', 'title']

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content']

class MusicDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)
    class Meta:
        model = Music
        fields = ['id', 'title', 'comments']

class ArtistDetailSerializer(serializers.ModelSerializer):
    musics = MusicDetailSerializer(many=True)
    musics_count = serializers.IntegerField(source='musics.count')
    # musics_count = MusicSerializer(many=True)
    class Meta:
        model = Artist
        fields = ['id', 'name', 'musics_count', 'musics']