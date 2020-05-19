from rest_framework import serializers
from .models import Task, ObjFile

# class LanguageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Language
#         fields = ('id', 'name', 'image')

class ObjFileSerializer(serializers.ModelSerializer):
    objFile = serializers.FileField()

    class Meta:
        model = ObjFile
        fields = ['objFile']

    # def create(self, validated_data):
    #     objFile = validated_data.pop('objFile')
    #     task_instance = Task.objects.last()
    #     instance = ObjFile.objects.create(**validated_data, task=task_instance)
    #     return instance

class NewTaskSerializer(serializers.ModelSerializer):
    configJSONFile = serializers.FileField()
    objFile = ObjFileSerializer(many=True, read_only=True)
    #objFile = serializers.FileField()

    class Meta:
        model = Task
        fields = ['created_at','configJSONFile', 'objFile']

 