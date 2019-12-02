from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from Alumno.models import Alumno
from rest_framework import filters
from Alumno.serializer import AlumnoSerializers


class AlumnoList(APIView):
    # METODO GET PARA SOLICITAR INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Alumno.objects.all()
        serializer = AlumnoSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AlumnoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class AlumnoDetail(APIView):

    def get_object(self, id):
        try:
            return Alumno.objects.get(id=id)
        except Alumno.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        Alumno = self.get_object(id)
        serializer = AlumnoSerializers(Alumno)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        Alumno = self.get_object(id)
        serializer = AlumnoSerializers(Alumno, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        Alumno = self.get_object(id)
        Alumno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AlumnosAPIView(generics.ListCreateAPIView):
    search_fields = ['nombre']
    filter_backends = (filters.SearchFilter,)
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers

class AlumnosEdadAPIView(generics.ListCreateAPIView):
    search_fields = ['edad']
    filter_backends = (filters.SearchFilter,)
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers
    
class AlumnosCarreraAPIView(generics.ListCreateAPIView):
    search_fields = ['carrera']
    filter_backends = (filters.SearchFilter,)
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializers

        



