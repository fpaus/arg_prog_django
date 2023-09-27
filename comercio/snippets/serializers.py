from rest_framework import serializers
from snippets.models import Snippet

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(required = False, allow_blank =True, max_length=100)
#     code = serializers.CharField()
#     language = serializers.CharField(required = False)
    
#     def create(self, data_validada):
#         return Snippet.objects.create(**data_validada)
    
#     def update(self, instancia, data_validada):
#         instancia.title = data_validada.get("title", instancia.title)
#         instancia.code = data_validada.get("code", instancia.code)
#         instancia.language = data_validada.get("language", instancia.language)
#         instancia.save()
#         return instancia

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "language"]