from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers
from supers import serializers



# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    
    if request.method == 'GET':
        
        super_type_name = request.query_params.get('super_type')
        print(super_type_name)
        query_set = Supers.objects.all()
        if super_type_name:
            query_set = query_set.filter(super_type__type=super_type_name)
        serializer = SupersSerializer(query_set, many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
@api_view(['GET', 'PUT', 'DELETE'])
def supers_details(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        