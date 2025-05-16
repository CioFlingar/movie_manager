from rest_framework import viewsets
from .models import MovieData
from .serializers import MovieSerializer
from django.shortcuts import render
from django.core.paginator import Paginator



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

def movie_list(request):
    movie_objects = MovieData.objects.all()

    movie_name = request.GET.get("movie_name")
    if movie_name != "" and movie_name is not None:
        movie_objects = movie_objects.filter(name__icontains=movie_name)

    paginator = Paginator(movie_objects, 2)
    page = request.GET.get("page")
    movie_objects = paginator.get_page(page)
    return render(request, "movies/movie_list.html", {"movie_objects": movie_objects})


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer
