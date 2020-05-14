from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Task
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
            request.POST.get("configJSONFile", "")
            serializer.save()
        if objSerializer.is_valid():
            request.POST.get("objFile", "")
            objSerializer.save()
            return Response(serializer.data, objSerializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
