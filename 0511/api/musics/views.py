from django.shortcuts import render, redirect, get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib import messages

from .models import Artist, Music, Comment
from .serializers import ArtistSerializer, ArtistDetailSerializer, MusicSerializer, MusicDetailSerializer, CommentSerializer
# Create your views here.

from faker import Faker

f=Faker()


@api_view(['GET'])
def artists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def artist_detail(request,artist_pk):
    artist = get_object_or_404(Artist, pk=artist_pk)
    serializer = ArtistDetailSerializer(artist)
    return Response(serializer.data)

@api_view(['GET'])
def music(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)
    comment=Comment()
    comment.music=music
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
def comment_pd(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method=='PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('성공적으로 수정되었습니다.')
    elif request.method=='DELETE':
        comment.delete()
        return Response('성공적으로 삭제 되었습니다.')