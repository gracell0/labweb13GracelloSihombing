from django.shortcuts import render
from rest_framework import generics
from basic_api.models import DRFPost
from basic_api.serializers import DRFPostSerializer
from django.db.models import Q

class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer

    def get_queryset(self):
        queryset = DRFPost.objects.all()
        search = self.request.query_params.get('search', None)
        rating = self.request.query_params.get('rating', None)

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(author__icontains=search)
            )

        if rating:
            queryset = queryset.filter(rating=rating)

        return queryset

class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
