from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from .tasks import populate_db_objects
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import CursorPagination
from rest_framework import filters

# Create your views here.
def HomeView(request):
    resp_row_1 = VideoDatabase.objects.all().order_by('-publishing_datetime')[:10]
    resp_row_2 = VideoDatabase.objects.all().order_by('-publishing_datetime')[10:20]
    context = {
        'video_objects_1': resp_row_1,
        'video_objects_2': resp_row_2,
    }
    #print(resp)
    return render(request, 'home.html', context)

@api_view(['GET'])
def get_stored_videos(request):
    video_objects = list(VideoDatabase.objects.order_by('-publishing_datetime').values())
    return Response(video_objects)

# Started Building Class for paginating response - Class based was simpler to implement over Function based despite
# Decorators available
class YoutubeResultsPaginator(CursorPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

class YoutubeSearchResults(generics.ListAPIView):
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter)
    ordering = ('-publishing_datetime')
    filterset_fields = ['title']
    queryset = VideoDatabase.objects.all()
    pagination_class = YoutubeResultsPaginator
    serializer_class = YoutubeSerializer
