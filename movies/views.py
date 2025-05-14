from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieSerializer



# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# @api_view(["GET"])
# def api_response(request):
#     movies= MovieData.objects.all()
#     serializer = MovieSerializer(movies, many=True)
#     return Response(serializer.data)


# @api_view(["POST"])
# def add_movie(request):
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer