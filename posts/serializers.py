from csv import writer
from rest_framework import serializers
from .models import Post, Comment
from accounts.models import User

# 기본 serializer
class PostBaseSerializer(serializers.Serializer):
    image = serializers.ImageField(required=False)
    content = serializers.CharField() #text를 여기는 charfield()로 받음
    created_at = serializers.DateTimeField(required=False)
    view_count = serializers.IntegerField()
    writer = serializers.IntegerField() #serializers는 foreign 키로 안 해주고 integer 키로 해줌(아이디를 고유숫자로 받음)
    bad_post = serializers.BooleanField() #기존에 없던 요소 추가해줌

    def create(self, validated_data):
        writer_id = validated_data['writer']
        post = Post.objects.create(
            content = validated_data['content'],
            view_count = validated_data['view_count'],
            writer = User.objects.get(id = writer_id), #과제1
        )
        return post
        # return Post.objects.create(validated_data)

# ModelSerializer
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'