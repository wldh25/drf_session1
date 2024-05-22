# posts > views.py
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .models import Post
from .serializers import *

class PostAPIView(APIView): # 컨트롤 마우스를 이용해서 어떤 걸 상속받는지 보면서 공부하기
    def post(self, request): #self는 원래 기본값, request : 가장 중요한 문법
        serializer = PostBaseSerializer(data = request.data) #번역기를 해주는 문장
        if serializer.is_valid(): #serialize 유효성 검사
            if serializer.validated_data['bad_post'] == True:
                return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save() #save가 되기 위해선 18번째 줄 is_valid()가 필수임
                return Response({"message": "post success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostAPIView2(APIView):
    def post(self, request):
        serializer = PostSerializer(data = request.data)
        print(serializer.initial_data)
        if serializer.is_valid():
            print(serializer.initial_data)
            if serializer.initial_data['bad_post'] == True:
                return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                print(serializer.data)
                return Response({"message": "post success"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetlistAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommentAPIView(APIView):
    def post(self, request):
        post_id = request.data.get('post')
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
        # User 객체를 writer 필드에 할당합니다.
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
# PostAPI_FBV 추가
@api_view(['POST'])
def PostAPI_FBV(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({"message": "post success"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#2가지 기능을 넣어줌
class PostListCreateMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request)
    
class PostListCreateGeneric(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.initial_data['bad_post'] == True:
            return Response({"message": "bad post" }, status=status.HTTP_400_BAD_REQUEST)
        return self.create(request)    
    
class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all() #모든 데이터를 갖고 놀겠다
    serializer_class = PostSerializer #번역기를 정해두는 것임 Serialize 통일 시켜야 함