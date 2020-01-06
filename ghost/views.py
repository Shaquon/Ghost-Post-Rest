# from django.shortcuts import render
from rest_framework import viewsets
from ghost.models import Post
from ghost.serializers import PostSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request):
        data = request.data
        print(data)
        post = Post.objects.create(
            is_boast=data['is_boast'],
            content=data['content']
        )
        return Response({
            'id': post.id
        })
        
    @action(detail=True, methods=['post'])
    def handle_upvote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.upvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'upvotes': post.upvotes
            })

    @action(detail=True, methods=['post'])
    def handle_downvote(self, request, pk=None):
        post = Post.objects.get(pk=pk)
        post.downvotes += 1
        post.save()
        return Response({
            'id': post.id,
            'downvotes': post.downvotes
        })