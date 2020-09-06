from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

# from myapp.serializers import UserSerializer

from .models import Album, Artist
from .serializers import (AlbumGETSerializer,ArtistListSerializer)


# class AlbumListView(generics.ListCreateAPIView):

#     queryset = Album.objects.all()
#     serializer_class = AlbumGETSerializer

#     def get_serializer_class(self):

#         assert self.serializer_class is not None, (
#             "'%s' should either include a `serializer_class` attribute, "
#             "or override the `get_serializer_class()` method."
#             % self.__class__.__name__
#         )

#         if self.request.method in ('POST', 'PUT'):
#             return AlbumGETSerializer
#         else:
#             return self.serializer_class


class AlbumListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumGETSerializer


class AlbumListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumGETSerializer
