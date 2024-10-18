from rest_framework.serializers import (
    ModelSerializer,
    HiddenField,
    CurrentUserDefault)
from cars.models import Car, Comment


class CarSerializer(ModelSerializer):
    owner = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['car', 'author']
