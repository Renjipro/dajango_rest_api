from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, ObjFile
from .serializers import NewTaskSerializer, ObjFileSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser


# class LanguageView(viewsets.ModelViewSet):
#     queryset = Language.objects.all()
#     serializer_class = LanguageSerializer

@api_view(['POST', 'GET'])
@parser_classes([MultiPartParser])
def TaskView(request):
    if request.method == 'POST':
        serializer = NewTaskSerializer(data=request.data)
        objSerializer = ObjFileSerializer(data=request.data)
        if serializer.is_valid():
            request.POST.get("objFile", "")
            request.POST.get("configJSONFile", "")
            #serializer.save()
        #if objSerializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        task = Task.objects.all()
        serializer = NewTaskSerializer(task, many=True)
        return Response(serializer.data)
