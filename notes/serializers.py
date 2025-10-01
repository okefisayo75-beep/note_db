from rest_framework import serializers
from .models import Note



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__" # ['title','content','created_at']