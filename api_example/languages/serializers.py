from rest_framework import serializers
from .models import Language, Task

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'image')

class NewTask(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name')