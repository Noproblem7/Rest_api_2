from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album, Artist, Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer


class ArtistAPIView(APIView):
    def get(self, request):
        queryset = Artist.objects.all()
        serializer = ArtistSerializer(queryset, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        context_error = {
            'status': 400,
            'data': serializer.data,
            'message': 'Xatolik'
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


class ArtistDetailAPIView(APIView):
    def get(self, request, id):
        try:
            artist = Artist.objects.get(id=id)
        except:
            context_error = {
                'status': 404,
                'message': 'Artist topilmadi'
            }
            return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

        if artist:
            serializer = ArtistSerializer(artist)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        context_error = {
            'status': 404,
            'message': 'artist topilmadi'
        }
        return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        artist = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=artist, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        queryset = Artist.objects.get(id=id)
        serializer = ArtistSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = Artist.objects.get(id=id)
        queryset.delete()
        context = {
            'status': 200,
            'message': 'artist ochirildi'
        }
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)


class AlbumAPIView(APIView):
    def get(self, request):
        album = Album.objects.all()
        serializer = AlbumSerializer(album, many=True)

        return Response(data=serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        context_error = {
            'status': 400,
            'data': serializer.data,
            'message': 'Xatolik'
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


class AlbumDetailAPIView(APIView):
    def get(self, request, id):
        try:
            album = Album.objects.get(id=id)
        except:
            context_error = {
                'status': 404,
                'message': 'albom topilmadi'
            }
            return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

        if album:
            serializer = AlbumSerializer(album)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        context_error = {
            'status': 404,
            'message': 'albom topilmadi'
        }
        return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        album = Album.objects.get(id=id)
        serializer = AlbumSerializer(instance=album, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        queryset = Album.objects.get(id=id)
        serializer = SongSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = Album.objects.get(id=id)
        queryset.delete()
        context = {
            'status': 200,
            'message': 'albom ochirildi'
        }
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)


class SongAPIView(APIView):
    def get(self, request):
        song = Song.objects.all()
        serializer = SongSerializer(song, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = SongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        context_error = {
            'status': 400,
            'data': serializer.data,
            'message': 'Xatolik'
        }

        return Response(data=context_error, status=status.HTTP_400_BAD_REQUEST)


class SongDetailAPIView(APIView):
    def get(self, request, id):
        try:
            queryset = Song.objects.get(id=id)
        except:
            context_error = {
                'status': 404,
                'message': 'qoshiq topilmadi'
            }
            return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

        if queryset:
            serializer = SongSerializer(queryset)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        context_error = {
            'status': 404,
            'message': 'qoshiq topilmadi'
        }
        return Response(data=context_error, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        queryset = Song.objects.get(id=id)
        serializer = SongSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        queryset = Song.objects.get(id=id)
        serializer = SongSerializer(instance=queryset, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        queryset = Song.objects.get(id=id)
        queryset.delete()
        context = {
            'status': 200,
            'message': 'qoshiq ochirildi'
        }
        return Response(data=context, status=status.HTTP_204_NO_CONTENT)
