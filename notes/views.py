from django.shortcuts import render
from .models import Note #db
from .serializers import NoteSerializer
from rest_framework import viewsets
from django.db.models import Q


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    ##DB creation......

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search', None)
        
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(content__icontains=search) 
            )
        
        return queryset




