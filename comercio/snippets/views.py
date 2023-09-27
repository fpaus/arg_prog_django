# Create your views here.
# @csrf_exempt
# def leer_id_y_retornar_json(request, pk):
#     print(pk)
#     if request.method == 'GET':
#         return JsonResponse({"ok": True}, safe=False)
#     else:
#         return JsonResponse({"ok": 'POST'}, safe=False)

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import viewsets

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# @api_view(["GET", "POST"])
# def snippet_list(request):
#     if request.method == "GET":
#         # listo listar
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data)
#         pass
#     elif request.method == "POST":
#         #Crear
#         serializer = SnippetSerializer(data = request.data)
#         if(serializer.is_valid()):
#             serializer.save()

#         pass


class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetails(APIView):

    authentication_classes = [BasicAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def _get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self._get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self._get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self._get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class SnippetViewSet(viewsets.ModelViewSet):
#     queryset=Snippet.objects.all()
#     serializer_class = SnippetSerializer
