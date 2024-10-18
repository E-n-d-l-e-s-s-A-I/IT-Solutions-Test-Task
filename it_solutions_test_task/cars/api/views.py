from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cars.models import Car
from .serializers import CarSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly, IsAuthenticateCreate


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticateCreate]


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):

    def get_queryset(self):
        car_pk = self.kwargs['pk']
        car = get_object_or_404(Car, pk=car_pk)
        return car.comments.all()

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        car_id = self.kwargs.get('pk')
        car = generics.get_object_or_404(Car, pk=car_id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(author=request.user, car=car)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )
