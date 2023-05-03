from django.shortcuts import render
import rest_framework.status as status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notes
from .serializers import *


@api_view(['GET', 'POST'])
def getNotes(request):
    notes = Notes.objects.all().order_by('-updated_at')
    serializer = NoteSerializer(notes, many=True)

    if request.method == "POST":
        data = request.data
        print("[POST] notes: ", data)
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        
    elif request.method == "GET":
        pass
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET', 'PUT', 'DELETE'])
def getNote(request, pk):
    notes = Notes.objects.get(id=pk)
    serializer = NoteSerializer(notes, many=False)

    if request.method == 'PUT':
        data = request.data
        print(data)
        serializer = NoteSerializer(notes, data=request.data)
        if serializer.is_valid():
            serializer.save()
    
    elif request.method == 'DELETE':
        notes.delete()
    
    elif request.method == 'GET':
        pass

    return Response(serializer.data, status=status.HTTP_200_OK)