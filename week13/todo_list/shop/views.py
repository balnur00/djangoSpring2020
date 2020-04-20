from django.http import Http404
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from shop.models import Author, Book
from shop.serializers import AuthorSerializer,BookSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action


class AuthorListViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(methods=['PUT'], detail=True)
    def set_rating(self, request, pk):
        author = self.get_object()
        # Variant 2
        # author = get_object_or_404(Author, id=pk)

        # Variant 1
        # try:
        #     author = Author.objects.get(id=pk)
        # except Author.DoesNotExist:
        #     raise Http404
        author.set_new_rating(request.data.get('value'))
        serializer = AuthorSerializer(author)
        return Response(serializer.data)


class BookViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer

    @action(methods=['POST'], detail=True)
    def test(self, request, pk):
        serializer = self.get_serializer()

        return Response('data')

    @action(methods=['POST'], detail=True)
    def test2(self, request, pk):
        serializer = self.get_serializer()

        return Response('data')

    @action(methods=['POST'], detail=True)
    def test3(self, request, pk):
        serializer = self.get_serializer()

        return Response('data')
